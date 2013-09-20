import sublime, sublime_plugin, os, os.path

class LilypondBuildCommand(sublime_plugin.WindowCommand):
  def run(self, cmd = None, shell_cmd = None, file_regex = "", line_regex = "", working_dir = "",
            encoding = "utf-8", env = {}, quiet = False, kill = False,
            word_wrap = True, syntax = "Packages/Text/Plain text.tmLanguage",
            # Catches "path" and "shell"
            **kwargs):
    lytempDir = os.path.join(working_dir, 'lytemp')
    if(not os.path.exists(lytempDir)):
      print('Creating ' + lytempDir)
      os.mkdir(lytempDir)
    self.window.run_command("exec", {
      "cmd": cmd,
      "shell_cmd": shell_cmd,
      "file_regex": file_regex,
      "line_regex": line_regex,
      "working_dir": working_dir,
      "encoding": encoding,
      "env": env,
      "quiet": quiet,
      "kill": kill,
      "word_wrap": word_wrap,
      "syntax": syntax
    },
      # Catches "path" and "shell"
      **kwargs)
