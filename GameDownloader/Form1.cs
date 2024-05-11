using System.Net;
using System.Runtime.CompilerServices;
namespace GameDownloader
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            button1.Enabled = false;
            using (WebClient wc = new WebClient())
        
    {
        wc.DownloadProgressChanged += wc_DownloadProgressChanged;
                wc.DownloadFileAsync(
                    // Param1 = Link of file
                    new System.Uri("https://github.com/Ameterius/minecraft-server-updates/raw/main/test_package.fxa"),
                    // Param2 = Path to save
                    "./game.zip"


                   
                );
    }
}

        private void wc_DownloadProgressChanged(object sender, DownloadProgressChangedEventArgs e)
        {
            progressBar1.Value = e.ProgressPercentage;
            if (progressBar1.Value == 100)
            {
                button1.Enabled = true;
                MessageBox.Show("Загрузка оконченна успешно!", "SHLaucnher", MessageBoxButtons.OK, MessageBoxIcon.Information);
            };
        }
    }
}
