using System;
using System.Collections.Generic;
using System.Linq;

namespace Day_2
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = System.IO.File.ReadAllLines(@"C:\Users\khoip\Desktop\AoC\Day 2\input.txt");
            char[] delimiterChars = { '-', ' ', ':' };
            List<int> minAmount = new List<int>();
            List<int> maxAmount = new List<int>();
            List<char> targetCharacter = new List<char>();
            List<String> password = new List<String>();
            int rightPasswordCounter = 0;
            int newPasswordCounter = 0;


            foreach(string line in input)
            {
                string[] temp = line.Split(delimiterChars);
                minAmount.Add(int.Parse(temp[0]));
                maxAmount.Add(int.Parse(temp[1]));
                targetCharacter.Add(char.Parse(temp[2]));
                password.Add(temp[4]);
            }

            for(int i = 0; i < password.Count; i++)
            {
                int count = password[i].Count(x => x == targetCharacter[i]);
                if (count >= minAmount[i] && count <= maxAmount[i])
                    rightPasswordCounter++;
            }
            Console.WriteLine(rightPasswordCounter);

            for (int i = 0; i < password.Count; i++)
            {
                if ((password[i][minAmount[i]-1] == targetCharacter[i]) ^ ((password[i][maxAmount[i]-1] == targetCharacter[i])))
                    newPasswordCounter++;
            }
            Console.WriteLine(newPasswordCounter);
        }
    }
}
