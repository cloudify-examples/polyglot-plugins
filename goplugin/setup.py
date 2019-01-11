########
# Copyright (c) 2019 Cloudify Platform Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
############


import setuptools
import os

files = None
for _,_,files in os.walk('golang_adapter/src/plugin'):
  files = files

setuptools.setup(
    name='golang-test-plugin',
    version='0.0.1',
    author='dfilppi',
    author_email='dfilppi@gmail.com',
    description='example golang plugin for cloudify',
    packages=['golang_adapter'],
    package_data = {'golang_adapter': [ 'src/plugin/'+ f for f in files ] },
    install_requires = [
      'cloudify-plugins-common'
    ],
    license='LICENSE'
)