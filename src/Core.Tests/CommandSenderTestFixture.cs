using System;
using NUnit.Framework;
using System.IO;
using PVC.Core;

namespace Core.Tests
{
	[TestFixture]
	public class CommandSenderTestFixture
	{
		[Test]
		public void Test_Send()
		{
			var command = "GX10";
			var sender = new CommandSender ();
			sender.SenduinoScriptPath = Path.GetFullPath ("testPythonScript.py");
			var result = sender.Send (command);
			var expectedResult = command + Environment.NewLine + "Finished";
			Assert.AreEqual (expectedResult, result, "Unexpected result");
		}
	}
}

