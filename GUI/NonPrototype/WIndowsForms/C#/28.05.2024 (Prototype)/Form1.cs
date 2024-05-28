using Microsoft.Win32;

namespace C_
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            this.FormClosing += new FormClosingEventHandler(Form1_FormClosing); // КОСТЫЛЬ
        }

        private void play_Click(object sender, EventArgs e)
        {

            RegistryKey localMachineKey = Registry.LocalMachine;
            RegistryKey key = Registry.CurrentUser.OpenSubKey(@"SOFTWARE\Ameteroz GitHub\SHLauncher\Setup", true);
            string Installed = key.GetValue("State").ToString();
            if (Installed == "True")
            {
                // Запуск майнкрафта
            };
            if (Installed == "False")
            {
                // Установка залупи
            }
        }
        private void Form1_FormClosing(object sender, FormClosingEventArgs e) // Костыль из-за свича форм
        {
            Environment.Exit(0);
        }

        private void settings_Click(object sender, EventArgs e) // Свич формы лаунчера на форму настроек
        {
            Form2 form2 = new Form2();
            this.Hide();
            form2.StartPosition = FormStartPosition.CenterParent;
            form2.ShowDialog();
            this.Close();
        }
    }
}
