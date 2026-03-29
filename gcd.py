#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:20:04 2026

@author: almila
"""

    
            
class EuclideanAlgorithm:
    
#This class implements the euclidean algorithm 
#to calculate the Greatest Common Divisor (GCD)
# and Least Common Multiple (LCM)
    

    def compute_gcd(self, a, b):
        
        
        """
Calculate the Greatest Common Divisor (GCD)
of two positive integers using the Euclidean Algorithm
        """     

        if a <= 0 or b <= 0:
            raise ValueError("Numbers must be positive integers.")

        while b != 0:
            a, b = b, a % b

        return a

    def compute_lcm(self, a, b):
# Extension method to calculate Least Common Multiple (LCM)
# using the formula: LCM = (a * b) / GCD

        gcd = self.compute_gcd(a, b)
        return abs(a * b) // gcd
    
    
def get_user_input():
    # This function gets valid input from the user
    while True:
        try:
            a = int(input("Enter first positive integer: "))
            b = int(input("Enter second positive integer: "))

            if a <= 0 or b <= 0:
                print("Error: Numbers must be positive.")
                continue

            return a, b

        except ValueError:
            print("Error: Please enter valid integers only.")
      


def main():
    algo = EuclideanAlgorithm()

    values = get_user_input()

    if values is not None:
        a, b = values
        gcd_result = algo.compute_gcd(a, b)
        lcm_result = algo.compute_lcm(a, b)
        
  
        print("GCD is:", gcd_result)
        print("LCM is:", lcm_result)


if __name__ == "__main__":
    main()           
            
            
            