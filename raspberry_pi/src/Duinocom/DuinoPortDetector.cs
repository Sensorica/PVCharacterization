using System;
using System.Threading;
using System.IO.Ports;
using System.Text;

namespace Duinocom
{
	public class DuinoPortDetector
	{
		public string Identifier = "";

		public DuinoPortDetector (string identifier)
		{
			Identifier = identifier;
		}

		public string Detect()
		{
			try
			{
				SerialPort port;
				string[] portNames = SerialPort.GetPortNames();

				for (int i = portNames.Length-1; i > 0; i--) // Iterate backwards because the port is often at the end.
				{
					var portName = portNames[i];
					port = new SerialPort(portName, 9600);
					if (IsPVC(port))
					{
						return portName;
					}
				}
			}
			catch (Exception)
			{
			}

			return String.Empty;
		}


		bool IsPVC(SerialPort port)
		{
			string returnMessage = "";
			try {
				if (port.IsOpen)
					port.Close ();

				port.Open ();

				Thread.Sleep (1500); // Fails if this delay is any shorter

				port.Write ("#");
				port.Write (port.NewLine);

				Thread.Sleep (500); // Fails if this delay is any shorter

				int count = port.BytesToRead;
				int intReturnASCII = 0;
				while (count > 0) {
					intReturnASCII = port.ReadByte ();
					returnMessage = returnMessage + Convert.ToChar (intReturnASCII);
					count--;
				}
			} catch {
			} finally {
				port.Close ();
			}
			if (returnMessage.Contains (Identifier)) {
				return true;
			} else {
				return false;
			}
		}
	}
}

