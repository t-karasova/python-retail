# Copyright 2021 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import subprocess


def test_import_products_gcs():
    output = str(
        subprocess.check_output('python product/import_products_gcs.py',
                                shell=True))

    assert re.match('.*import products from google cloud source request.*',
                    output)
    assert re.match('.*input_uris: "gs://.*/products.json".*', output)
    assert re.match('.*the operation was started.*', output)
    assert re.match(
        '.*projects/.*/locations/global/catalogs/default_catalog/branches/0/operations/import-products.*',
        output)

    assert re.match('.*number of successfully imported products.*316.*', output)
