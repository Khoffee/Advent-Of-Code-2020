using System;

namespace Day_3
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] input = System.IO.File.ReadAllLines(@"C:\Users\khoip\Desktop\AoC\Day 3\input.txt");
            long totalCount =
                Sloper(1, 1, input) *
                Sloper(3, 1, input) *
                Sloper(5, 1, input) *
                Sloper(7, 1, input) *
                Sloper(1, 2, input);
            Console.WriteLine(totalCount);

        }

        public static long Sloper(int right, int down, string[] input)
        {
            long treeCounter = 0;
            int xPosition = 0;
            int yPosition = 0;

            for (int i = 0; i < input.Length; i++)
            {
                xPosition += right;
                yPosition += down;
                xPosition = xPosition % input[i].Length;
                if (yPosition >= input.Length)
                    break;
                if (input[yPosition][xPosition] == '#')
                    treeCounter++;
            }
            return treeCounter;
        }
    }
}
