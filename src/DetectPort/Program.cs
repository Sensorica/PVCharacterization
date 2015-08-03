using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO.Ports; //required for SerialPort class
using System.Threading;
using PVC.Core;

namespace SerialPortCommunicationExample
{
	class Program
	{

		static void Main(string[] args)
		{
			Console.WriteLine (new SerialPortDetector ().Detect ());
		}

	}
}