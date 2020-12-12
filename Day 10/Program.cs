using System;
using System.Collections.Concurrent;
using System.Collections.Generic;

namespace Day_10
{
    public static class Program
    {
        static int oneDif = 0;
        static int twoDif = 0;
        static int threeDif = 1;
        static List<int> input = new List<int>();
        static List<int> inputTwo;
        static ConcurrentDictionary<long, long> cache = new ConcurrentDictionary<long, long>();


        static void Main(string[] args)
        {
            string[] inputString = System.IO.File.ReadAllLines(@"C:\Users\khoip\Desktop\AoC\Day 10\input.txt");

            foreach(string word in inputString)
            {
                input.Add(int.Parse(word));
            }

            input.Sort();

            JoltDiff(input[0]);

            for (int i = 1; i < input.Count; i++)
            {
                int difference = input[i] - input[i - 1];

                JoltDiff(difference);
            }

            //Part Two
            inputTwo = new List<int>(input);
            inputTwo.Insert(0, 0);
            inputTwo.Add(input[input.Count - 1] + 3);
            Console.WriteLine(RecursiveShit(0));
        }

        public static void JoltDiff(int num)
        {
            switch (num)
            {
                case 1:
                    oneDif++;
                    break;
                case 2:
                    twoDif++;
                    break;
                case 3:
                    threeDif++;
                    break;
                default:
                    break;
            }
        }

        public static Func<T1, TResult> Memoize<T1, TResult>(this Func<T1, TResult> func)
        {
            var cache = new ConcurrentDictionary<T1, TResult>();
            return key => cache.GetOrAdd(key, func);
        }

        public static long RecursiveShit(int index)
        {
            if (index == (inputTwo.Count - 1))
                return 1;

            if (cache.ContainsKey(index))
                return cache[index];
            long total = 0;
            for (int i = index + 1; i < inputTwo.Count; i++)
            {
                if (inputTwo[i] - inputTwo[index] <= 3)
                    total = total + RecursiveShit(i);
            }
            cache[index] = total;
            return total;

        }
    }

}
