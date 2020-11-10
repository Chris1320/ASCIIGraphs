#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
MIT License
Copyright (c) 2020 Chris1320

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sys
import time

class ASCIIGraphs():
    """
    The class for creating graphs, splashes,
    animations, and progress bars.
    """

    def __init__(self):
        """
        Initialization method of ASCIIGraphs() class.
        """

        self.VERSION = "0.0.1.0"

    def progress_bar(self, length, description='Loading...', progress_bar_length=20):
        """
        Print progress bar while waiting for a specified time.

        :param float length: How long the progress bar will show up.
        :param str description: The description of the loading screen.
        :param int progress_bar_length: The length of the progress bar.

        :returns None:
        """

        length = float(length)
        start = time.time()
        end = start + length
        iteration_counter = 0
        while True:
            iteration_counter = end - time.time()
            total_items = length
            percent = float(iteration_counter) / total_items
            spaces = ' ' * int(round(percent * progress_bar_length))
            hashes = '#' * (progress_bar_length - len(spaces))
            per = int(100 - round(percent * 100))
            if per > 100:
                per = 100

            sys.stdout.write("\r{0} [{1}] {2}%".format(description,
                hashes + spaces, per))
            sys.stdout.flush()
            if int(100 - round(percent * 100)) >= 100:
                print('\r')
                if length > 1:
                    time.sleep(1)

                else:
                    time.sleep(length)

                break

            else:
                if length > 1:
                    time.sleep(1)

                else:
                    time.sleep(length)

                continue

    def progress_bar_manual(self, description='Loading...', iteration_counter=0, total_items=100, progress_bar_length=20):
        """
        Print progress bar manually.

        :param str description: Description of the loading screen.
        :param int iteration_counter: Incremental counter
        :param int total_items: total number items
        :param int progress_bar_length: Progress bar length

        :returns None:
        """

        percent = float(iteration_counter) / total_items
        hashes = '#' * int(round(percent * progress_bar_length))
        spaces = ' ' * (progress_bar_length - len(hashes))
        sys.stdout.write("\r{0} [{1}] {2}%".format(description,
            hashes + spaces, int(round(percent * 100))))
        sys.stdout.flush()
        if total_items == iteration_counter:
            print("\r")

    def animated_loading_screen(self, length, description='Loading...', animation='loading', delay=0.15):
        """
        Print an animated loading screen while waiting for a specified time.

        :param float length: How long the loading screen will show up.
        :param str description: Message in the loading screen.
        :param str animation: Animation to use. (Can either be `loading` or `swapcase`)
        :param float delay: Delay on each frame.

        :returns None:
        """

        if animation.lower() == 'loading':
            length = float(time.time()) + float(length)
            splashes = ['-', '\\', '|', '/']
            iterator = 0
            while time.time() < length:
                sys.stdout.write("\r{0} {1}".format(description,
                    splashes[iterator]))
                sys.stdout.flush()
                iterator += 1
                if iterator > 3 or iterator < 0:
                    iterator = 0

                time.sleep(delay)

            sys.stdout.write('\r{0}{1}'.format(description, '  '))
            sys.stdout.flush()
            print('\r')

            return None

        elif animation.lower() == 'swapcase':
            length = float(time.time()) + float(length)
            characters = list(description)
            iterator = 0
            while time.time() < length:
                if characters[iterator].isupper():
                    characters[iterator] = characters[iterator].lower()

                elif characters[iterator].islower():
                    characters[iterator] = characters[iterator].upper()

                else:
                    pass

                desc = ''
                for character in characters:
                    desc += character

                sys.stdout.write("\r{0}".format(desc))
                if characters[iterator].isupper():
                    characters[iterator] = characters[iterator].lower()

                elif characters[iterator].islower():
                    characters[iterator] = characters[iterator].upper()

                else:
                    pass

                iterator += 1
                if iterator > (len(characters) - 1):
                    iterator = 0

                time.sleep(delay)

            sys.stdout.write('\r{0}{1}'.format(description, '  '))
            sys.stdout.flush()
            print('\r')

            return None

        else:
            print("[i] Unknown animation `{0}`!".format(animation))
            return None

    def animated_loading_screen_manual(self, last_load=False, description='Loading...', animation='loading', delay=0.15):
        r"""
        Print an animated loading screen.

        :param bool last_load: If True, print a \r in the screen, which means the end of the loading.
        :param str description: Message in the loading screen.
        :param str animation: Animation to use. (Either `loading` or `swapcase`)
        :param float delay: Length of each animation to play.

        :returns None:
        """

        if animation.lower() == 'loading':
            splashes = ['-', '\\', '|', '/']
            iterator = 0
            while not iterator >= (len(splashes) - 1):
                sys.stdout.write("\r{0} {1}".format(description,
                    splashes[iterator]))
                sys.stdout.flush()
                iterator += 1
                if iterator > 3 or iterator < 0:
                    iterator = 0

                time.sleep(delay)

            if last_load is True:
                sys.stdout.write('\r{0}{1}'.format(description, '  '))
                sys.stdout.flush()
                print('\r')
                return None

            else:
                return None

        elif animation.lower() == 'swapcase':
            characters = list(description)
            iterator = 0
            while True:
                if characters[iterator].isupper():
                    characters[iterator] = characters[iterator].lower()

                elif characters[iterator].islower():
                    characters[iterator] = characters[iterator].upper()

                else:
                    pass

                desc = ''
                for character in characters:
                    desc += character

                sys.stdout.write("\r{0}".format(desc))
                if characters[iterator].isupper():
                    characters[iterator] = characters[iterator].lower()

                elif characters[iterator].islower():
                    characters[iterator] = characters[iterator].upper()

                else:
                    pass

                iterator += 1
                if iterator > (len(characters) - 1):
                    break

                time.sleep(delay / (len(characters) - 1))

            if last_load is True:
                sys.stdout.write('\r{0}{1}'.format(description, '  '))
                sys.stdout.flush()
                print('\r')

            return None

        else:
            print("[i] Unknown animation `{0}`!".format(animation))
            return None
