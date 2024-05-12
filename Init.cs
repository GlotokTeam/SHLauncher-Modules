using Microsoft.Win32;
using System;
using System.Threading.Tasks;


// Перенос модуля init.py на более лёгкий формат без GIL
namespace InitC_
{
    internal class Program
    {
        static void Main(string[] args)
        {
            RegistryKey key = Registry.CurrentUser.OpenSubKey(@"SOFTWARE\Ameteroz GitHub\SHLauncher\Setup", true);
            key.SetValue("Branch", "main");
            key.SetValue("CurrentVer", "0.1"); // Меняйте в зависимости от установочного пакета, типо если есть все обновления то ставте чё-нибудь другое
            key.SetValue("State", "True");
            key.SetValue("README", "This a SHLauncher Directory, please don't change any values!"); // Типо хуйня
        }
    }
}
