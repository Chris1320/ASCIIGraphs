import unittest
import shutil
import time
import os

shutil.copy("../asciigraphs.py", "./asciigraphs.py")
import asciigraphs
os.remove("./asciigraphs.py")

class TestCases(unittest.TestCase):

    def test_progress_bar(self):
        print("\n[TEST] Testing ASCIIGraphs().progress_bar()\n")
        asciigraphs.ASCIIGraphs().progress_bar(3, "Testing...")
        print()

    def test_progress_bar_manual(self):
        print("\n[TEST] Testing ASCIIGraphs().progress_bar_manual()\n")
        _ = 0
        while _ < 100:
            asciigraphs.ASCIIGraphs().progress_bar_manual("Testing again...", _, 100)
            time.sleep(0.25)
            _ += 5

        print("\n[TEST] Testing ASCIIGraphs().progress_bar_manual() overflow\n")

        _ = 0
        while _ < 150:
            asciigraphs.ASCIIGraphs().progress_bar_manual("Testing overflow...", _, 100)
            time.sleep(0.25)
            _ += 5

        print()

    def test_animated_loading_screen(self):
        print("\n[TEST] Testing ASCIIGraphs().animated_loading_screen()\n")
        asciigraphs.ASCIIGraphs().animated_loading_screen(3, "Testing....", "loading")
        asciigraphs.ASCIIGraphs().animated_loading_screen(3, "Testing....", "swapcase")
        asciigraphs.ASCIIGraphs().animated_loading_screen(3, "Testing....", "somethingwrong")
        print()

    def test_animated_loading_screen_manual(self):
        print("\n[TEST] Testing ASCIIGraphs().animated_loading_screen_manual()\n")
        _ = 0
        while _ < 100:
            if _ >= 100:
                lastloop = True

            else:
                lastloop = False

            asciigraphs.ASCIIGraphs().animated_loading_screen_manual(lastloop, "Manual animated loading...", "loading")

            _ += 5

        print("\n[TEST] Testing ASCIIGraphs().animated_loading_screen_manual() overflow\n")

        _ = 0
        while _ < 150:
            if _ >= 150:
                lastloop = True

            else:
                lastloop = False

            asciigraphs.ASCIIGraphs().animated_loading_screen_manual(lastloop, "Manual animated loading overflow...", "loading")

            _ += 5

        print()

if __name__ == "__main__":
    unittest.main()