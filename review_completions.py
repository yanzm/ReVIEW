# coding:utf-8
import sublime, sublime_plugin, re

class TypeScriptCompletionListener(sublime_plugin.EventListener):

    def get_completion(self, trigger, contents):
        return ([
            (trigger, contents)
        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)

    def on_query_completions(self, view, prefix, locations):
        if not view.file_name().endswith('.re'):
            # .re ファイル以外は無視
            return []

        try:
            # カーソル位置を含む行のRegion（行の最初から最後）を取得
            l = view.line(locations[0])
            # 行の先頭からカーソルまでの文字を取得
            t = view.substr(sublime.Region(l.a, locations[0])).encode('utf-8')

            # 直前の文字が #@hoge かどうかチェック
            m = re.search('(?<=#@)\w*$', t)
            if m != None:
                tag = m.group(0)

                if t.startswith('#@'):
                    # 行頭が #@ の場合は、そのまま補完
                    return ([
                        ("#@mapfile\t#@mapfile( ... ) ... #@end", "#@mapfile($1)\n$2\n#@end"),
                        ("#@mapoutput\t#@mapoutput( ... ) ... #@end", "#@mapoutput($1)\n$2\n#@end"),
                        ("#@maprange\t#@maprange( ... ) ... #@end", "#@maprange($1,$2)\n$3\n#@end"),
                        ("#@provide\t#@provide", "#@provide"),
                        ("#@require\t#@require", "#@require"),
                        ("#@warn\t#@warn( ... )", "#@warn($1)")
                    ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
                else:
                    # 行の途中から #@ の場合は、改行して補完
                    return ([
                        ("#@mapfile\t#@mapfile( ... ) ... #@end", "\n#@mapfile($1)\n$2\n#@end\n"),
                        ("#@mapoutput\t#@mapoutput( ... ) ... #@end", "\n#@mapoutput($1)\n$2\n#@end\n"),
                        ("#@maprange\t#@maprange( ... ) ... #@end", "\n#@maprange($1,$2)\n$3\n#@end\n"),
                        ("#@provide\t#@provide", "\n#@provide\n"),
                        ("#@require\t#@require", "\n#@require\n"),
                        ("#@warn\t#@warn( ... )", "\n#@warn($1)\n")
                    ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)

            # 直前の文字が @<list>{ かどうかチェック
            m = re.search('(?<=@<list>{)$', t)
            if m != None:
                regions = view.find_all("^//list\[[^]]*\]")
                list_ids = []
                for region in regions:
                    m = re.search('^//list\[([^]]*)\]', view.substr(region))
                    exp = m.group(1)
                    list_ids.append((exp, exp))

                return (list_ids, sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)


            # 直前の文字が @hoge かどうかチェック
            m = re.search('(?<=@)\w*$', t)
            if m != None:
                tag = m.group(0)

                return ([
                    ("@ami\t@<ami>{ ... }", "@<ami>{$1}"),
                    ("@b\t@<b>{ ... }", "@<b>{$1}"),
                    ("@bib\t@<bib>{ ... }", "@<bib>{$1}"),
                    ("@bou\t@<bou>{ ... }", "@<bou>{$1}"),
                    ("@br\t@<br>{}", "@<br>{}"),
                    ("@chap\t@<chap>{ ... }", "@<chap>{$1}"),
                    ("@chapref\t@<chapref>{ ... }", "@<chapref>{$1}"),
                    ("@code\t@<code>{ ... }", "@<code>{$1}"),
                    ("@comment\t@<comment>{ ... }", "@<comment>{$1}"),
                    ("@em\t@<em>{ ... }", "@<em>{$1}"),
                    ("@fn\t@<fn>{ ... }", "@<fn>{$1}"),
                    ("@hd\t@<hd>{ ... }", "@<hd>{$1}"),
                    ("@href\t@<href>{ ... }", "@<href>{$1}"),
                    ("@i\t@<i>{ ... }", "@<i>{$1}"),
                    ("@icon\t@<icon>{ ... }", "@<icon>{$1}"),
                    ("@img\t@<img>{ ... }", "@<img>{$1}"),
                    ("@kw\t@<kw>{ ... }", "@<kw>{$1,$2}"),
                    ("@list\t@<list>{ ... }", "@<list>{$1}"),
                    ("@m\t@<m>{ ... }", "@<m>{$1}"),
                    ("@raw\t@<raw>{ ... }", "@<raw>{|$1|$2}"),
                    ("@ruby\t@<ruby>{ ... }", "@<ruby>{$1,$2}"),
                    ("@strong\t@<strong>{ ... }", "@<strong>{$1}"),
                    ("@table\t@<table>{ ... }", "@<table>{$1}"),
                    ("@title\t@<title>{ ... }", "@<title>{$1}"),
                    ("@tt\t@<tt>{ ... }", "@<tt>{$1}"),
                    ("@tti\t@<tti>{ ... }", "@<tti>{$1}"),
                    ("@ttb\t@<ttb>{ ... }", "@<ttb>{$1}"),
                    ("@u\t@<u>{ ... }", "@<u>{$1}"),
                    ("@uchar\t@<uchar>{ ... }", "@<uchar>{$1}")
                ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)

            # 直前の文字が //hoge かどうかチェック
            m = re.search('(?<=//)\w*$', t)
            if m != None:
                tag = m.group(0)

                if t.startswith('//'):
                    return ([
                        ("//bibpaper\t//bibpaper[][]{ ... //}", "//bibpaper[$1][$2]{\n$3\n//}"),
                        ("//cmd\t//cmd{ ... //}", "//cmd{\n$1\n//}"),
                        ("//emlist\t//emlist{ ... //}", "//emlist{\n$1\n//}"),
                        ("//footnote\t//footnote[][]", "//footnote[$1][$2]"),
                        ("//graph\t//graph[][][]{ ... //}", "//graph[$1][$2][$3]{\n$4\n//}"),
                        ("//image\t//image[][]{ ... //}", "//image[$1][$2]{\n$3\n//}"),
                        ("//indepimage\t//indepimage[]", "//indepimage[$1]"),
                        ("//lead\t//lead{ ... //}", "//lead{\n$1\n//}"),
                        ("//list\t//list[][]{ ... //}", "//list[$1][$2]{\n$3\n//}"),
                        ("//listnum\t//listnum[][]{ ... //}", "//listnum[$1][$2]{\n$3\n//}"),
                        ("//noindent\t//noindent", "//noindent"),
                        ("//quote\t//quote{ ... //}", "//quote{\n$1\n//}"),
                        ("//raw\t//raw[ ... //]", "//raw[|$1|$2]"),
                        ("//source\t//source[]{ ... //}", "//source[$1]{\n$2\n//}"),
                        ("//table\t//table[][]{ ... //}", "//table[$1][$2]{\n$3\n//}"),
                        ("//texequation\t//texequation{ ... //}", "//texequation{\n$1\n//}"),
                        ("//emlist\t//emlist{ ... //}", "//emlist{\n$1\n//}")
                    ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
                else:
                    return ([
                        ("//bibpaper\t//bibpaper[][]{ ... //}", "\n\n//bibpaper[$1][$2]{\n$3\n//}\n"),
                        ("//cmd\t//cmd{ ... //}", "\n\n//cmd{\n$1\n//}\n"),
                        ("//emlist\t//emlist{ ... //}", "\n\n//emlist{\n$1\n//}\n"),
                        ("//footnote\t//footnote[][]", "\n\n//footnote[$1][$2]\n"),
                        ("//graph\t//graph[][][]{ ... //}", "\n\n//graph[$1][$2][$3]{\n$4\n//}\n"),
                        ("//image\t//image[][]{ ... //}", "\n\n//image[$1][$2]{\n$3\n//}\n"),
                        ("//indepimage\t//indepimage[]", "\n\n//indepimage[$1]\n"),
                        ("//lead\t//lead{ ... //}", "\n\n//lead{\n$1\n//}\n"),
                        ("//list\t//list[][]{ ... //}", "\n\n//list[$1][$2]{\n$3\n//}\n"),
                        ("//listnum\t//listnum[][]{ ... //}", "\n\n//listnum[$1][$2]{\n$3\n//}\n"),
                        ("//noindent\t//noindent", "\n\n//noindent\n"),
                        ("//quote\t//quote{ ... //}", "\n\n//quote{\n$1\n//}\n"),
                        ("//raw\t//raw[ ... //]", "\n\n//raw[|$1|$2]\n"),
                        ("//source\t//source[]{ ... //}", "\n\n//source[$1]{\n$2\n//}\n"),
                        ("//table\t//table[][]{ ... //}", "\n\n//table[$1][$2]{\n$3\n//}\n"),
                        ("//texequation\t//texequation{ ... //}", "\n\n//texequation{\n$1\n//}\n"),
                        ("//emlist\t//emlist{ ... //}", "\n\n//emlist{\n$1\n//}\n")
                    ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)


        except:
            print 'please save as utf-8'

        return ([
            ("ami\t@<ami>{ ... }", "@<ami>{$1}"),
            ("b\t@<b>{ ... }", "@<b>{$1}"),
            ("bib\t@<bib>{ ... }", "@<bib>{$1}"),
            ("bibpaper\t//bibpaper[][]{ ... //}", "//bibpaper[$1][$2]{\n$3\n//}"),
            ("bou\t@<bou>{ ... }", "@<bou>{$1}"),
            ("br\t@<br>{}", "@<br>{}"),
            ("chap\t@<chap>{ ... }", "@<chap>{$1}"),
            ("chapref\t@<chapref>{ ... }", "@<chapref>{$1}"),
            ("cmd\t//cmd{ ... //}", "//cmd{\n$1\n//}"),
            ("code\t@<code>{ ... }", "@<code>{$1}"),
            ("column\t===[column] ... ===[/column]", "===[column] $1\n$2\n===[/column]"),
            ("comment\t@<comment>{ ... }", "@<comment>{$1}"),
            ("em\t@<em>{ ... }", "@<em>{$1}"),
            ("emlist\t//emlist{ ... //}", "//emlist{\n$1\n//}"),
            ("fn\t@<fn>{ ... }", "@<fn>{$1}"),
            ("footnote\t//footnote[][]", "//footnote[$1][$2]"),
            ("graph\t//graph[][][]{ ... //}", "//graph[$1][$2][$3]{\n$4\n//}"),
            ("hd\t@<hd>{ ... }", "@<hd>{$1}"),
            ("href\t@<href>{ ... }", "@<href>{$1}"),
            ("i\t@<i>{ ... }", "@<i>{$1}"),
            ("icon\t@<icon>{ ... }", "@<icon>{$1}"),
            ("image\t//image[][]{ ... //}", "//image[$1][$2]{\n$3\n//}"),
            ("img\t@<img>{ ... }", "@<img>{$1}"),
            ("indepimage\t//indepimage[]", "//indepimage[$1]"),
            ("kw\t@<kw>{ ... }", "@<kw>{$1,$2}"),
            ("lead\t//lead{ ... //}", "//lead{\n$1\n//}"),
            ("li\t@<list>{ ... }", "@<list>{$1}"),
            ("list\t//list[][]{ ... //}", "//list[$1][$2]{\n$3\n//}"),
            ("listnum\t//listnum[][]{ ... //}", "//listnum[$1][$2]{\n$3\n//}"),
            ("m\t@<m>{ ... }", "@<m>{$1}"),
            ("mapfile\t#@mapfile( ... ) ... #@end", "#@mapfile($1)\n$2\n#@end"),
            ("mapoutput\t#@mapoutput( ... ) ... #@end", "#@mapoutput($1)\n$2\n#@end"),
            ("maprange\t#@maprange( ... ) ... #@end", "#@maprange($1,$2)\n$3\n#@end"),
            ("noindent\t//noindent", "//noindent"),
            ("provide\t#@provide", "#@provide"),
            ("quote\t//quote{ ... //}", "//quote{\n$1\n//}"),
            ("raw\t@<raw>{ ... }", "@<raw>{|$1|$2}"),
            ("raw\t//raw[ ... //]", "//raw[|$1|$2]"),
            ("require\t#@require", "#@require"),
            ("ruby\t@<ruby>{ ... }", "@<ruby>{$1,$2}"),
            ("source\t//source[]{ ... //}", "//source[$1]{\n$2\n//}"),
            ("strong\t@<strong>{ ... }", "@<strong>{$1}"),
            ("table\t//table[][]{ ... //}", "//table[$1][$2]{\n$3\n//}"),
            ("tb\t@<table>{ ... }", "@<table>{$1}"),
            ("texequation\t//texequation{ ... //}", "//texequation{\n$1\n//}"),
            ("title\t@<title>{ ... }", "@<title>{$1}"),
            ("tt\t@<tt>{ ... }", "@<tt>{$1}"),
            ("tti\t@<tti>{ ... }", "@<tti>{$1}"),
            ("ttb\t@<ttb>{ ... }", "@<ttb>{$1}"),
            ("u\t@<u>{ ... }", "@<u>{$1}"),
            ("uchar\t@<uchar>{ ... }", "@<uchar>{$1}"),
            ("warn\t#@warn( ... )", "#@warn($1)"),
            ("emlist\t//emlist{ ... //}", "//emlist{\n$1\n//}")
        ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)


