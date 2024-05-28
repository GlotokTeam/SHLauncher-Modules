namespace C_
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            play = new Button();
            settings = new Button();
            SuspendLayout();
            // 
            // play
            // 
            play.Location = new Point(561, 294);
            play.Name = "play";
            play.Size = new Size(75, 23);
            play.TabIndex = 0;
            play.Text = "Играть";
            play.UseVisualStyleBackColor = true;
            play.Click += play_Click;
            // 
            // settings
            // 
            settings.Location = new Point(12, 294);
            settings.Name = "settings";
            settings.Size = new Size(75, 23);
            settings.TabIndex = 1;
            settings.Text = "Настройки";
            settings.UseVisualStyleBackColor = true;
            settings.Click += settings_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(648, 329);
            Controls.Add(settings);
            Controls.Add(play);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Icon = (Icon)resources.GetObject("$this.Icon");
            MinimizeBox = false;
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
        }

        #endregion

        private Button play;
        private Button settings;
    }
}
