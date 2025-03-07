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

from .services.catalog_service import CatalogServiceClient
from .services.catalog_service import CatalogServiceAsyncClient
from .services.completion_service import CompletionServiceClient
from .services.completion_service import CompletionServiceAsyncClient
from .services.prediction_service import PredictionServiceClient
from .services.prediction_service import PredictionServiceAsyncClient
from .services.product_service import ProductServiceClient
from .services.product_service import ProductServiceAsyncClient
from .services.search_service import SearchServiceClient
from .services.search_service import SearchServiceAsyncClient
from .services.user_event_service import UserEventServiceClient
from .services.user_event_service import UserEventServiceAsyncClient

from .types.catalog import Catalog
from .types.catalog import ProductLevelConfig
from .types.catalog_service import GetDefaultBranchRequest
from .types.catalog_service import GetDefaultBranchResponse
from .types.catalog_service import ListCatalogsRequest
from .types.catalog_service import ListCatalogsResponse
from .types.catalog_service import SetDefaultBranchRequest
from .types.catalog_service import UpdateCatalogRequest
from .types.common import Audience
from .types.common import ColorInfo
from .types.common import CustomAttribute
from .types.common import FulfillmentInfo
from .types.common import Image
from .types.common import Interval
from .types.common import PriceInfo
from .types.common import Promotion
from .types.common import Rating
from .types.common import UserInfo
from .types.completion_service import CompleteQueryRequest
from .types.completion_service import CompleteQueryResponse
from .types.import_config import BigQuerySource
from .types.import_config import CompletionDataInputConfig
from .types.import_config import GcsSource
from .types.import_config import ImportCompletionDataRequest
from .types.import_config import ImportCompletionDataResponse
from .types.import_config import ImportErrorsConfig
from .types.import_config import ImportMetadata
from .types.import_config import ImportProductsRequest
from .types.import_config import ImportProductsResponse
from .types.import_config import ImportUserEventsRequest
from .types.import_config import ImportUserEventsResponse
from .types.import_config import ProductInlineSource
from .types.import_config import ProductInputConfig
from .types.import_config import UserEventImportSummary
from .types.import_config import UserEventInlineSource
from .types.import_config import UserEventInputConfig
from .types.prediction_service import PredictRequest
from .types.prediction_service import PredictResponse
from .types.product import Product
from .types.product_service import AddFulfillmentPlacesMetadata
from .types.product_service import AddFulfillmentPlacesRequest
from .types.product_service import AddFulfillmentPlacesResponse
from .types.product_service import CreateProductRequest
from .types.product_service import DeleteProductRequest
from .types.product_service import GetProductRequest
from .types.product_service import ListProductsRequest
from .types.product_service import ListProductsResponse
from .types.product_service import RemoveFulfillmentPlacesMetadata
from .types.product_service import RemoveFulfillmentPlacesRequest
from .types.product_service import RemoveFulfillmentPlacesResponse
from .types.product_service import SetInventoryMetadata
from .types.product_service import SetInventoryRequest
from .types.product_service import SetInventoryResponse
from .types.product_service import UpdateProductRequest
from .types.purge_config import PurgeMetadata
from .types.purge_config import PurgeUserEventsRequest
from .types.purge_config import PurgeUserEventsResponse
from .types.search_service import SearchRequest
from .types.search_service import SearchResponse
from .types.user_event import CompletionDetail
from .types.user_event import ProductDetail
from .types.user_event import PurchaseTransaction
from .types.user_event import UserEvent
from .types.user_event_service import CollectUserEventRequest
from .types.user_event_service import RejoinUserEventsMetadata
from .types.user_event_service import RejoinUserEventsRequest
from .types.user_event_service import RejoinUserEventsResponse
from .types.user_event_service import WriteUserEventRequest

__all__ = (
    "CatalogServiceAsyncClient",
    "CompletionServiceAsyncClient",
    "PredictionServiceAsyncClient",
    "ProductServiceAsyncClient",
    "SearchServiceAsyncClient",
    "UserEventServiceAsyncClient",
    "AddFulfillmentPlacesMetadata",
    "AddFulfillmentPlacesRequest",
    "AddFulfillmentPlacesResponse",
    "Audience",
    "BigQuerySource",
    "Catalog",
    "CatalogServiceClient",
    "CollectUserEventRequest",
    "ColorInfo",
    "CompleteQueryRequest",
    "CompleteQueryResponse",
    "CompletionDataInputConfig",
    "CompletionDetail",
    "CompletionServiceClient",
    "CreateProductRequest",
    "CustomAttribute",
    "DeleteProductRequest",
    "FulfillmentInfo",
    "GcsSource",
    "GetDefaultBranchRequest",
    "GetDefaultBranchResponse",
    "GetProductRequest",
    "Image",
    "ImportCompletionDataRequest",
    "ImportCompletionDataResponse",
    "ImportErrorsConfig",
    "ImportMetadata",
    "ImportProductsRequest",
    "ImportProductsResponse",
    "ImportUserEventsRequest",
    "ImportUserEventsResponse",
    "Interval",
    "ListCatalogsRequest",
    "ListCatalogsResponse",
    "ListProductsRequest",
    "ListProductsResponse",
    "PredictRequest",
    "PredictResponse",
    "PredictionServiceClient",
    "PriceInfo",
    "Product",
    "ProductDetail",
    "ProductInlineSource",
    "ProductInputConfig",
    "ProductLevelConfig",
    "ProductServiceClient",
    "Promotion",
    "PurchaseTransaction",
    "PurgeMetadata",
    "PurgeUserEventsRequest",
    "PurgeUserEventsResponse",
    "Rating",
    "RejoinUserEventsMetadata",
    "RejoinUserEventsRequest",
    "RejoinUserEventsResponse",
    "RemoveFulfillmentPlacesMetadata",
    "RemoveFulfillmentPlacesRequest",
    "RemoveFulfillmentPlacesResponse",
    "SearchRequest",
    "SearchResponse",
    "SearchServiceClient",
    "SetDefaultBranchRequest",
    "SetInventoryMetadata",
    "SetInventoryRequest",
    "SetInventoryResponse",
    "UpdateCatalogRequest",
    "UpdateProductRequest",
    "UserEvent",
    "UserEventImportSummary",
    "UserEventInlineSource",
    "UserEventInputConfig",
    "UserEventServiceClient",
    "UserInfo",
    "WriteUserEventRequest",
)
