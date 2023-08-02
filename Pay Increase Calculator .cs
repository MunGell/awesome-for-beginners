//RICHARD AKINKUNMI 29496470
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pay_Increase
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btn_ShowPay_Click(object sender, EventArgs e)
        {
            int initialCompensation;
            double pay = 0.0;
            if (int.TryParse(txt_input.Text, out initialCompensation))
            {
                list_TeacherPay.Items.Add("Year\tPay");
                for (int i = 1; i <= 5; i++)
                {
                    if (i == 1)
                    {
                        pay = initialCompensation;
                        list_TeacherPay.Items.Add(i + "\t$" + pay);
                    }
                    else
                    {
                        double per = (double)5 / 100;
                        pay = pay + (pay * per);
                        list_TeacherPay.Items.Add(i + "\t$" + Math.Round(pay, 2));
                    }
                }
            }
            else
            {
                MessageBox.Show("Invalid amount!! Please enter valid input !!");
                txt_input.Clear();
                list_TeacherPay.Items.Clear();
            }
        }
        private void btn_Exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
