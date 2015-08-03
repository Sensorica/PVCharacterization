using System;
using System.IO;
using System.Diagnostics;

namespace PVC.Core
{
	public class CommandSender
	{
		public string SenduinoScriptPath = Path.GetFullPath ("senduino.py");
		public string CommandLogPath = Path.GetFullPath ("commandLog.txt");

		public string Send(string arduinoCommand)
		{

			ProcessStartInfo start = new ProcessStartInfo();
			start.FileName = "python";
			start.Arguments = string.Format ("{0} {1}", SenduinoScriptPath, arduinoCommand);
			start.UseShellExecute = false;
			start.RedirectStandardOutput = true;
			string result = "";

			using(Process process = Process.Start(start))
			{
				using(StreamReader reader = process.StandardOutput)
				{
					result = reader.ReadToEnd();

				}
			}

			LogCommand (arduinoCommand, result.Trim());

			return result.Trim();
		}

		public void LogCommand(string arduinoCommand, string arduinoResult)
		{
			File.AppendAllText (CommandLogPath, "Command:" + Environment.NewLine);
			File.AppendAllText (CommandLogPath, arduinoCommand + Environment.NewLine);
			File.AppendAllText (CommandLogPath, "Result:" + Environment.NewLine);
			File.AppendAllText (CommandLogPath, arduinoResult + Environment.NewLine);
			File.AppendAllText (CommandLogPath, Environment.NewLine + Environment.NewLine);
		}
	}
}

