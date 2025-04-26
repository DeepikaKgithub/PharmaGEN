#!/usr/bin/env python3
"""
PharmaGPT Runner Script
-----------------------
This script helps users set up and run the PharmaGPT application.
It checks for dependencies, prompts for API key if needed, and launches the app.
"""

import os
import sys
import subprocess

def check_dependencies():
    """Check if required packages are installed."""
    try:
        import gradio
        import google.generativeai
        import fpdf
        return True
    except ImportError as e:
        print(f"Missing dependency: {e}")
        return False

def install_dependencies():
    """Install required dependencies."""
    print("Installing required dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("Failed to install dependencies. Please install them manually using:")
        print("pip install -r requirements.txt")
        return False

def check_api_key():
    """Check if Gemini API key is set."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("\n" + "="*50)
        print("No Gemini API key found in environment variables.")
        print("You can set it permanently with:")
        if os.name == 'nt':  # Windows
            print("set GEMINI_API_KEY=your-key-here")
        else:  # Unix/Linux/Mac
            print("export GEMINI_API_KEY='your-key-here'")
        
        api_key = input("Please enter your Gemini API key (or press Enter to skip): ").strip()
        if api_key:
            os.environ["GEMINI_API_KEY"] = api_key
            print("API key set for this session.")
        print("="*50 + "\n")

def main():
    """Main function to run the application."""
    print("="*50)
    print("Welcome to PharmaGPT Setup")
    print("="*50)
    
    # Check and install dependencies if needed
    if not check_dependencies():
        print("Some dependencies are missing.")
        choice = input("Would you like to install them now? (y/n): ").lower()
        if choice == 'y':
            if not install_dependencies():
                return
        else:
            print("Please install the required dependencies and try again.")
            return
    
    # Check API key
    check_api_key()
    
    # Run the application
    print("Starting PharmaGPT...")
    try:
        from app import create_interface
        demo = create_interface()
        demo.launch(share=True)
    except Exception as e:
        print(f"Error starting PharmaGPT: {e}")
        print("Please check the error message and try again.")

if __name__ == "__main__":
    main()