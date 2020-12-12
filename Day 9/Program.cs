using System;

namespace Day_9
{
    public class Program
    {
        static void Main(string[] args)
        {
            string[] input = System.IO.File.ReadAllLines(@"C:\Users\khoip\Desktop\AoC\Day 9\input.txt");
            long[] values = Array.ConvertAll(input, x => Int64.Parse(x));

            int preamble = 25;
            int correctIndex = 0;
            long correctValue = 0;

            for (int i = preamble; i < values.Length; i++)
            {
                bool flag = false;
                for(int j = i - preamble; j < i; j++)
                {
                    for(int k = i - preamble; k < i; k++)
                    {
                        if (j == k)
                            continue;

                        var sum = values[j] + values[k];

                        if (values[i] == sum)
                        {
                            flag = true;
                            goto SumFound;
                        }
                    }
                }
            SumFound:
                if (!flag)
                {
                    correctIndex = i;
                    correctValue = values[i];
                    Console.WriteLine("This is it: " + values[i]);
                    Console.WriteLine(PartTwo(correctValue, correctIndex, values));
                    break;
                }
            }
        }

        public static long PartTwo(long target, int index, long[] values)
        {
            long finalValue = 0;
            for(int i = 0; i < index; i++)
            {
                long minValue = values[i];
                long maxValue = 0;

                if (values[i] < minValue)
                    minValue = values[i];
                if (values[i] > maxValue)
                    maxValue = values[i];
                long cumsum = values[i];
                for (int j = i + 1; j < index; j++)
                {
                    if (values[j] < minValue)
                        minValue = values[j];
                    if (values[j] > maxValue)
                        maxValue = values[j];
                    cumsum += values[j];
                    if (cumsum == target)
                    {
                        Console.WriteLine("Part Two");
                        Console.WriteLine(minValue + " " + maxValue);
                        finalValue = minValue + maxValue;
                        goto FinalPlaceThing;
                    }
                    if (cumsum > target)
                        break;
                }
            }
        FinalPlaceThing:
            return finalValue;
        }
    }
}