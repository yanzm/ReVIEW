import sublime, sublime_plugin, re, os


class ReviewLintCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        error_message = ""

        # key check
        # image
        error_message += self.check(self.view, ["image"], "img")
        # list
        error_message += self.check(self.view, ["list", "listnum"], "list")
        # table
        error_message += self.check(self.view, ["table"], "table")
        # footnote
        error_message += self.check(self.view, ["footnote"], "fn")

        # image exist check
        error_message += self.checkImage(self.view)

        if not error_message:
            error_message = "No error"

        output_view = self.view.window().get_output_panel("hoge")
        self.view.window().run_command("show_panel", {"panel": "output.hoge"})
        output_view.set_read_only(False)
        edit = output_view.begin_edit()
        output_view.insert(edit, output_view.size(), error_message)
        output_view.end_edit(edit)
        output_view.set_read_only(True)

    def check(self, view, block_commands, inline_command):
        defined_list_keys = []

        # pick up key of all //command[]
        for block_command in block_commands:
            regions = view.find_all("^//" + block_command + "\[[^]]*\]")
            for region in regions:
                m = re.search(
                    "^//" + block_command + "\[([^]]*)\]",
                    view.substr(region))
                defined_list_keys.append(m.group(1))

        # pick up each key of @<command>{}
        regions = view.find_all("@<" + inline_command + ">\{[^}]+\}")
        error_message = ""
        for region in regions:
            m = re.search(
                "@<" + inline_command + ">\{([^}]+)\}",
                view.substr(region))
            key = m.group(1)
            if key not in defined_list_keys:
                (row, col) = view.rowcol(region.a)
                error_message += (
                    str(row + 1) + ": Error key not found ("
                    + self.view.substr(region) + ")\n")

        return error_message

    def checkImage(self, view):
        error_message = ""

        file_name = view.file_name()
        index = file_name.rfind("/") + 1
        filename = file_name[0:index] + "images/" + file_name[index:-3]

        print(filename)

        block_command = "image"
        regions = view.find_all("^//" + block_command + "\[[^]]*\]")
        for region in regions:
            m = re.search(
                "^//" + block_command + "\[([^]]*)\]",
                view.substr(region))
            key = m.group(1)
            # png
            filepath = filename + "-" + key + ".png"

            if os.path.exists(filepath):
                continue
            filepath = filename + "-" + key + ".jpg"
            if os.path.exists(filepath):
                continue
            filepath = filename + "-" + key + ".jpeg"
            if os.path.exists(filepath):
                continue

            (row, col) = view.rowcol(region.a)
            error_message += (
                str(row + 1) +
                ": Error image not exists (" +
                self.view.substr(region) + ")\n")

        return error_message
