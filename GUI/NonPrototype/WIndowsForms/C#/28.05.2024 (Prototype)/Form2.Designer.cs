namespace C_
{
    partial class Form2
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            nickname = new TextBox();
            RamBar = new TrackBar();
            label2 = new Label();
            ((System.ComponentModel.ISupportInitialize)RamBar).BeginInit();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Location = new Point(12, 9);
            label1.Name = "label1";
            label1.Size = new Size(64, 15);
            label1.TabIndex = 1;
            label1.Text = "Никнейм :";
            // 
            // nickname
            // 
            nickname.Location = new Point(12, 27);
            nickname.Name = "nickname";
            nickname.Size = new Size(177, 23);
            nickname.TabIndex = 2;
            // 
            // RamBar
            // 
            RamBar.LargeChange = 1024;
            RamBar.Location = new Point(12, 74);
            RamBar.Maximum = 2;
            RamBar.Name = "RamBar";
            RamBar.Size = new Size(260, 45);
            RamBar.TabIndex = 3;
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Location = new Point(12, 56);
            label2.Name = "label2";
            label2.Size = new Size(88, 15);
            label2.TabIndex = 4;
            label2.Text = "Память (ОЗУ) :";
            // 
            // Form2
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(635, 329);
            Controls.Add(label2);
            Controls.Add(RamBar);
            Controls.Add(nickname);
            Controls.Add(label1);
            Name = "Form2";
            Text = "Form2";
            ((System.ComponentModel.ISupportInitialize)RamBar).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label1;
        private TextBox nickname;
        private TrackBar RamBar;
        private Label label2;
    }
}