About
======

ReVIEW plugin for Sublime Text 2


How to Install
======

#### 1. Package Control をインストール

すでにインストールしている場合はこのステップは必要ありません。

[View] - [Show Console] からコンソールを表示し、コンソールに以下のコマンドを入力

```import urllib2,os;
pf='Package Control.sublime-package';
url = 'http://sublime.wbond.net/' +pf.replace( ' ','%20' );
ipp = sublime.installed_packages_path();
os.makedirs( ipp ) if not os.path.exists(ipp) else None;
urllib2.install_opener( urllib2.build_opener( urllib2.ProxyHandler( )));
open( os.path.join( ipp, pf), 'wb' ).write( urllib2.urlopen( url ).read());
print( 'Please restart Sublime Text to finish installation');```

実行したら Sublime Text 2 を再起動


#### 2. Command + Shift + p（Windows では Ctrl + Shift + p）で Command Palette を開き、Add Repository を選択
#### 3. 下の方にリポジトリの URL を入力するフォームが表示されるので、https://github.com/yanzm/ReVIEW と入力して Enter を押す
#### 4. リポジトリを追加したら、Command + Shift + p（Windows では Ctrl + Shift + p）で再度 Command Palette を開き、今度は Install Package を選択
#### 5. インストールするパッケージを聞かれるので、ReVIEW を選択
#### 6. インストールが完了したら Sublime Text 2 を再起動
