import sublime, sublime_plugin

class ReviewJumpCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.find_all("(^={1,4}(\{([^\}]+)\})?)\s(.*)")
		items = []
		for region in regions:
			items.append(self.view.substr(region))
		self.items = items
		self.regions = regions
		self.view.window().show_quick_panel(items, self.on_done)
		# self.view.insert(edit, 0, "Hello, World!")

	def on_done(self, picked):
		if picked == -1:
			return
		
		self.view.show(self.regions[picked].a)

		self.view.sel().clear()
		self.view.sel().add(self.regions[picked])
#		self.view.sel().add(sublime.Region(self.regions[picked].a))

		print self.view.sel()


