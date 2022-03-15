# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for ListCatalogs
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-retail


# [START retail_v2_generated_CatalogService_ListCatalogs_sync]
from google.cloud import retail_v2


def sample_list_catalogs():
    # Create a client
    client = retail_v2.CatalogServiceClient()

    # Initialize request argument(s)
    request = retail_v2.ListCatalogsRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.list_catalogs(request=request)

    # Handle the response
    for response in page_result:
        print(response)

# [END retail_v2_generated_CatalogService_ListCatalogs_sync]
