//
//  ViewController.swift
//  swift-calculator
//
//  Created by Mark Kipyegon Koskei on 18/02/2016.
//
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var display: UILabel!
    
    var userInput: Bool = false

    @IBAction func appendDigit(_ sender: UIButton) {
        let digit = sender.currentTitle
        if userInput {
        display.text = display.text! + digit!
        }
        else {
            display.text = digit
            userInput = true
        }
    }
    
    @IBAction func operate(_ sender: UIButton) {
        let operation = sender.currentTitle!
        if userInput {
            enter()
        }
        switch operation {
            case "＊": performOperation { $0 * $1}
            case "∕" : performOperation { $1 / $0}
            case "+" : performOperation { $0 + $1}
            case "-" : performOperation { $1 - $0}
            case "√" : performSqrt { sqrt($0)}
        default : break
        }
    }
    
    func performOperation(_ operation: (Double, Double) -> Double) {
        if operandStack.count >= 2 {
            displayValue = operation(operandStack.removeLast(), operandStack.removeLast())
            enter()
        }
    }
    
    func performSqrt(_ operation: (Double) -> Double) {
        if operandStack.count >= 1 {
            displayValue = operation(operandStack.removeLast())
            enter()
        }
    }

    var operandStack: Array<Double> = Array<Double>()
    
    @IBAction func enter() {
        userInput = false
        operandStack.append(displayValue)
        print("operandStack = \(operandStack)")
    }
    
    var displayValue: Double {
        get {
            return NumberFormatter().number(from: display.text!)!.doubleValue
        }
        set{
            display.text = "\(newValue)"
            userInput = false
        }
    }
}
