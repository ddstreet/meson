# Copyright 2016-2021 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import unittest

from run_tests import (
    Backend
)

from .baseplatformtests import BasePlatformTests

class PythonTests(BasePlatformTests):
    '''
    Tests that verify compilation of python extension modules
    '''

    def test_bad_versions(self):
        if self.backend is not Backend.ninja:
            raise unittest.SkipTest(f'Skipping python tests with {self.backend.name} backend')

        testdir = os.path.join(self.src_root, 'test cases', 'python', '8 different python versions')

        # The test is configured to error out with MESON_SKIP_TEST
        # in case it could not find python
        with self.assertRaises(unittest.SkipTest):
            self.init(testdir, extra_args=['-Dpython=not-python'])
        self.wipe()

        # While dir is an external command on both Windows and Linux,
        # it certainly isn't python
        with self.assertRaises(unittest.SkipTest):
            self.init(testdir, extra_args=['-Dpython=dir'])
        self.wipe()
