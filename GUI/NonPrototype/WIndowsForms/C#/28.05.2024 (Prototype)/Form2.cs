using Microsoft.Win32;
using System;
using System.Windows.Forms;

namespace C_
{
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
            this.FormClosing += new FormClosingEventHandler(Form2_FormClosing);
            RegistryKey key = Registry.CurrentUser.CreateSubKey(@"SOFTWARE\Ameteroz GitHub\SHLauncher\Player", true);
            nickname.Text = key.GetValue("nickname").ToString();
            nickname.TextChanged += nickname_TextChanged;

        }

        private void Form2_FormClosing(object sender, FormClosingEventArgs e)
        {
            RegistryKey key = Registry.CurrentUser.CreateSubKey(@"SOFTWARE\Ameteroz GitHub\SHLauncher\Player", true);
            key.SetValue("nickname", nickname.Text);

            Form1 form1 = new Form1();
            this.Hide();
            form1.StartPosition = FormStartPosition.CenterParent;
            form1.ShowDialog();
            this.Close();
        }

        private void nickname_TextChanged(object sender, System.EventArgs e)
        {
            string unchecked_text = nickname.Text;
            unchecked_text = nickname.Text.Replace(" ", "");
            nickname.Text = unchecked_text;
            nickname.SelectionStart = nickname.Text.Length;
        }
    }
}