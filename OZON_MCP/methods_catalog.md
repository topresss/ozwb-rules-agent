# Ozon API 完整方法目录（中文详细说明·卡片式）

- 方法总数：**466**
- 卖家 API：**420**
- 广告绩效 API：**46**

> 说明：中文说明是在原始接口标题基础上，结合操作标识、接口路径和所属模块整理的便于阅读的扩展释义，用于帮助理解接口用途；具体请求参数、返回字段和业务限制仍应以完整 JSON Schema 与 Ozon 官方接口定义为准。

## 卖家 API

方法数量：**420**

### 高级订阅专属方法

方法数量：**10**

#### 1. `AnalyticsAPI_AnalyticsGetData`

**中文说明：** 获取 Ozon 店铺的经营分析数据，可按照请求中指定的指标、维度和时间范围返回统计结果，用于制作销售、流量或商品表现分析。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/analytics/data`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 2. `AnalyticsAPI_AnalyticsProductQueries`

**中文说明：** 获取买家通过哪些搜索词找到卖家的商品，以及相关搜索表现数据，用于分析关键词覆盖和商品搜索流量。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/analytics/product-queries`
- **安全级别：** 写入
- **订阅要求：** PREMIUM

---

#### 3. `AnalyticsAPI_AnalyticsProductQueriesDetails`

**中文说明：** 获取指定商品搜索词的详细统计结果，用于进一步查看某个关键词对应的商品表现和搜索效果。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/analytics/product-queries/details`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 4. `ChatAPI_ChatSendMessage`

**中文说明：** 向指定买家会话发送文字消息，用于订单沟通、售后答疑或处理买家的咨询。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/chat/send/message`
- **安全级别：** 写入
- **订阅要求：** PREMIUM_PLUS

---

#### 5. `ChatAPI_ChatStart`

**中文说明：** 根据指定对象创建一个新的买家聊天会话，用于开始订单、商品或售后相关沟通。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/chat/start`
- **安全级别：** 写入
- **订阅要求：** PREMIUM_PLUS

---

#### 6. `FinanceAPI_GetRealizationByDayReportV1`

**中文说明：** 获取指定日期的商品销售与结算明细，用于核对当日销售、费用、退款和实际结算情况。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/finance/realization/by-day`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PLUS

---

#### 7. `ProductPricesDetails`

**中文说明：** 获取商品价格的详细组成信息，包括平台价格相关数据，供价格检查、竞争力分析和定价决策使用。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/prices/details`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PRO

---

#### 8. `SearchQueriesAPI_SearchQueriesText`

**中文说明：** 按照输入文本查找相关的 Ozon 搜索词及统计信息，用于关键词调研、标题优化和选品分析。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/search-queries/text`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PRO

---

#### 9. `SearchQueriesAPI_SearchQueriesTop`

**中文说明：** 获取 Ozon 平台热门搜索词及其相关统计信息，用于发现市场需求、选品方向和高热度关键词。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/search-queries/top`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PRO

---

#### 10. `ChatAPI_ChatReadV2`

**中文说明：** 将指定聊天中的消息标记为已读，用于同步客服处理状态并避免重复处理未读消息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/chat/read`
- **安全级别：** 写入
- **订阅要求：** PREMIUM_PLUS

---

### Ozon 平台活动

方法数量：**8**

#### 1. `Promos`

**中文说明：** 获取 Ozon 平台当前可见的促销活动列表，用于查看可报名或正在进行的活动及其基础信息。

- **HTTP 方法：** `GET`
- **接口路径：** `/v1/actions`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `PromosCandidates`

**中文说明：** 获取可参加活动的商品列表，用于查看平台促销机会、处理折扣申请以及管理商品报名。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/actions/candidates`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `promos_task_approve`

**中文说明：** 用于同意折扣申请，具体用于查看平台促销机会、处理折扣申请以及管理商品报名。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/actions/discounts-task/approve`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `promos_task_decline`

**中文说明：** 拒绝折扣申请，对指定对象执行取消、删除、拒绝或归档处理，并用于查看平台促销机会、处理折扣申请以及管理商品报名；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/actions/discounts-task/decline`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 5. `promos_task_list`

**中文说明：** 获取折扣申请列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查看平台促销机会、处理折扣申请以及管理商品报名。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/actions/discounts-task/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `PromosProducts`

**中文说明：** 获取参加活动的商品列表，用于查看平台促销机会、处理折扣申请以及管理商品报名。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/actions/products`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `PromosProductsActivate`

**中文说明：** 将商品加入活动，用于查看平台促销机会、处理折扣申请以及管理商品报名。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/actions/products/activate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 8. `PromosProductsDeactivate`

**中文说明：** 将商品移出活动，用于查看平台促销机会、处理折扣申请以及管理商品报名。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/actions/products/deactivate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 卖家自建活动

方法数量：**18**

#### 1. `SellerActionsArchive`

**中文说明：** 将活动归档，对指定对象执行取消、删除、拒绝或归档处理，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/archive`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 2. `SellerActionsChangeActivity`

**中文说明：** 启用或停用活动，根据提交的参数更新已有配置、内容或业务状态，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/change-activity`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `SellerActionsCreateDiscount`

**中文说明：** 创建“折扣”活动，根据提交的参数创建新的业务记录，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/create/discount`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `SellerActionsCreateDiscountWithCondition`

**中文说明：** 创建“满额折扣”活动，根据提交的参数创建新的业务记录，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/create/discount-with-condition`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `SellerActionsCreateInstallment`

**中文说明：** 创建“免息分期”活动，根据提交的参数创建新的业务记录，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/create/installment`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `SellerActionsCreateMultiLevelDiscount`

**中文说明：** 创建“按金额分级折扣”活动，用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/create/multi-level-discount`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `SellerActionsCreateVoucher`

**中文说明：** 创建“优惠码折扣”活动，根据提交的参数创建新的业务记录，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/create/voucher`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 8. `SellerActionsList`

**中文说明：** 获取活动列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `SellerActionsProductsAdd`

**中文说明：** 将商品加入活动，用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/products/add`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 10. `SellerActionsProductsCandidates`

**中文说明：** 获取可参加活动的商品列表，用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/products/candidates`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 11. `SellerActionsProductsDelete`

**中文说明：** 将商品移出活动，对指定对象执行取消、删除、拒绝或归档处理，并用于创建、维护卖家自己的优惠活动并管理参与商品；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/products/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 12. `SellerActionsProductsList`

**中文说明：** 获取参加活动的商品列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/products/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 13. `SellerActionsUpdateDiscount`

**中文说明：** 更新“折扣”活动，根据提交的参数更新已有配置、内容或业务状态，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/update/discount`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 14. `SellerActionsUpdateDiscountWithCondition`

**中文说明：** 更新“满额折扣”活动，根据提交的参数更新已有配置、内容或业务状态，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/update/discount-with-condition`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 15. `SellerActionsUpdateInstallment`

**中文说明：** 更新“免息分期”活动，根据提交的参数更新已有配置、内容或业务状态，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/update/installment`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 16. `SellerActionsUpdateMultiLevelDiscount`

**中文说明：** 更新“按金额分级折扣”活动，用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/update/multi-level-discount`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 17. `SellerActionsUpdateVoucher`

**中文说明：** 更新“优惠码折扣”活动，根据提交的参数更新已有配置、内容或业务状态，并用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/update/voucher`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 18. `SellerActionsVoucherGet`

**中文说明：** 获取 CSV 格式优惠码文件，用于创建、维护卖家自己的优惠活动并管理参与商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller-actions/voucher/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 分析报告

方法数量：**6**

#### 1. `AnalyticsAPI_AverageDeliveryTime`

**中文说明：** 获取平均配送时长分析，用于分析店铺履约、库存和商品周转情况，辅助经营决策。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/analytics/average-delivery-time`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `AnalyticsAPI_AverageDeliveryTimeDetails`

**中文说明：** 获取平均配送时长详细分析，返回指定对象的详细信息，便于后续判断或处理，并用于分析店铺履约、库存和商品周转情况，辅助经营决策。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/analytics/average-delivery-time/details`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `AverageDeliveryTimeSummary`

**中文说明：** 获取平均配送时长汇总分析，用于分析店铺履约、库存和商品周转情况，辅助经营决策。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/analytics/average-delivery-time/summary`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `AnalyticsAPI_AnalyticsStocks`

**中文说明：** 获取商品库存分析数据，用于查看库存数量、销售消耗和潜在缺货或积压情况。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/analytics/stocks`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `AnalyticsAPI_StocksTurnover`

**中文说明：** 获取商品库存周转指标，包括库存覆盖和周转等级等数据，用于识别缺货、滞销和补货风险。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/analytics/turnover/stocks`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `AnalyticsAPI_AnalyticsGetStockOnWarehousesV2`

**中文说明：** 获取库存与商品报告，用于分析店铺履约、库存和商品周转情况，辅助经营决策。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/analytics/stock_on_warehouses`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### Ozon 类目属性与特征

方法数量：**4**

#### 1. `DescriptionCategoryAPI_GetAttributes`

**中文说明：** 获取类目属性列表，用于进行类目匹配、获取必填属性并填写合规的商品资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/description-category/attribute`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `DescriptionCategoryAPI_GetAttributeValues`

**中文说明：** 获取属性可选值字典，用于进行类目匹配、获取必填属性并填写合规的商品资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/description-category/attribute/values`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `DescriptionCategoryAPI_SearchAttributeValues`

**中文说明：** 用于搜索属性字典值，具体用于进行类目匹配、获取必填属性并填写合规的商品资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/description-category/attribute/values/search`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `DescriptionCategoryAPI_GetTree`

**中文说明：** 用于类目与商品类型树，具体用于进行类目匹配、获取必填属性并填写合规的商品资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/description-category/tree`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 退货出库

方法数量：**8**

#### 1. `ReturnAPI_GiveoutGetBarcode`

**中文说明：** 用于退货出库条码值，具体用于查询和领取从 Ozon 退回给卖家的货物。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/return/giveout/barcode`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `ReturnAPI_GiveoutBarcodeReset`

**中文说明：** 生成新条码，用于查询和领取从 Ozon 退回给卖家的货物。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/return/giveout/barcode-reset`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `ReturnAPI_GiveoutGetPDF`

**中文说明：** 获取退货出库 PDF 条码，用于查询和领取从 Ozon 退回给卖家的货物。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/return/giveout/get-pdf`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `ReturnAPI_GiveoutGetPNG`

**中文说明：** 获取退货出库 PNG 条码，用于查询和领取从 Ozon 退回给卖家的货物。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/return/giveout/get-png`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `ReturnAPI_GiveoutInfo`

**中文说明：** 获取退货出库信息，返回指定对象的详细信息，便于后续判断或处理，并用于查询和领取从 Ozon 退回给卖家的货物。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/return/giveout/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `ReturnAPI_GiveoutIsEnabled`

**中文说明：** 检查是否支持凭条码领取退货出库，用于查询和领取从 Ozon 退回给卖家的货物。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/return/giveout/is-enabled`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `ReturnAPI_GiveoutList`

**中文说明：** 获取退货出库列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询和领取从 Ozon 退回给卖家的货物。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/return/giveout/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `returnsCompanyFBSInfo`

**中文说明：** 用于FBS 退货数量，具体用于查询和领取从 Ozon 退回给卖家的货物。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/returns/company/fbs/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### FBO 与 FBS 商品退货

方法数量：**4**

#### 1. `returnsList`

**中文说明：** 获取FBO 和 FBS 商品退货信息，用于处理 FBO/FBS 售后退货以及自动销毁设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/returns/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `UtilizationHistory`

**中文说明：** 获取自动销毁设置变更历史，根据提交的参数更新已有配置、内容或业务状态，并用于处理 FBO/FBS 售后退货以及自动销毁设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/returns/settings/utilization/history`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `UtilizationInfo`

**中文说明：** 获取自动销毁设置，返回指定对象的详细信息，便于后续判断或处理，并用于处理 FBO/FBS 售后退货以及自动销毁设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/returns/settings/utilization/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `UtilizationUpdate`

**中文说明：** 更新自动销毁设置，根据提交的参数更新已有配置、内容或业务状态，并用于处理 FBO/FBS 售后退货以及自动销毁设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/returns/settings/utilization/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### rFBS 商品退货

方法数量：**8**

#### 1. `ReturnsAPI_ReturnsRfbsActionSet`

**中文说明：** 提交 rFBS 退货可执行操作，用于处理 rFBS 买家退货、验货、退款和补偿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/returns/rfbs/action/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `RFBSReturnsAPI_ReturnsRfbsCompensateV2`

**中文说明：** 退还部分商品款，用于处理 rFBS 买家退货、验货、退款和补偿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/returns/rfbs/compensate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `RFBSReturnsAPI_ReturnsRfbsGetV2`

**中文说明：** 获取退货申请信息，返回指定对象的详细信息，便于后续判断或处理，并用于处理 rFBS 买家退货、验货、退款和补偿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/returns/rfbs/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `RFBSReturnsAPI_ReturnsRfbsListV2`

**中文说明：** 获取退货申请列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于处理 rFBS 买家退货、验货、退款和补偿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/returns/rfbs/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `RFBSReturnsAPI_ReturnsRfbsReceiveReturnV2`

**中文说明：** 确认收到待检查商品，用于处理 rFBS 买家退货、验货、退款和补偿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/returns/rfbs/receive-return`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `RFBSReturnsAPI_ReturnsRfbsRejectV2`

**中文说明：** 拒绝退货申请，对指定对象执行取消、删除、拒绝或归档处理，并用于处理 rFBS 买家退货、验货、退款和补偿；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/returns/rfbs/reject`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 7. `RFBSReturnsAPI_ReturnsRfbsReturnMoneyV2`

**中文说明：** 向买家退款，用于处理 rFBS 买家退货、验货、退款和补偿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/returns/rfbs/return-money`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 8. `RFBSReturnsAPI_ReturnsRfbsVerifyV2`

**中文说明：** 批准退货申请，用于处理 rFBS 买家退货、验货、退款和补偿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/returns/rfbs/verify`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 配送

方法数量：**5**

#### 1. `DeliveryCheck`

**中文说明：** 检查买家地址是否可配送，查看当前处理状态、校验结果或执行进度，并用于判断配送可用性并查询配送、自提点等基础信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/delivery/check`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `DeliveryMap`

**中文说明：** 在地图上绘制点位，用于判断配送可用性并查询配送、自提点等基础信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/delivery/map`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `DeliveryPointInfo`

**中文说明：** 获取自提点信息，返回指定对象的详细信息，便于后续判断或处理，并用于判断配送可用性并查询配送、自提点等基础信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/delivery/point/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `DeliveryAPI_DeliveryPointList`

**中文说明：** 获取自提点列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于判断配送可用性并查询配送、自提点等基础信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/delivery/point/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `DeliveryCheckout`

**中文说明：** 获取可用配送方案，查看当前处理状态、校验结果或执行进度，并用于判断配送可用性并查询配送、自提点等基础信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/delivery/checkout`
- **安全级别：** 写入
- **订阅要求：** PREMIUM

---

### FBO 配送

方法数量：**14**

#### 1. `PostingAPI_GetPostingFboCancelReasonList`

**中文说明：** 获取FBO 发货取消原因，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbo/cancel-reason/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `SupplierAPI_SupplierAvailableWarehouses`

**中文说明：** 用于Ozon 仓库负载情况，具体用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `GET`
- **接口路径：** `/v1/supplier/available_warehouses`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `SupplyOrderBundle`

**中文说明：** 用于供货单或供货申请的商品组成，具体用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/bundle`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `SupplyOrderAPI_SupplyOrderDetails`

**中文说明：** 获取供货申请详细信息，返回指定对象的详细信息，便于后续判断或处理，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/details`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `SupplyOrderAPI_SupplyOrderPassCreate`

**中文说明：** 获取填写司机和车辆信息，根据提交的参数创建新的业务记录，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/pass/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `SupplyOrderAPI_SupplyOrderPassStatus`

**中文说明：** 获取司机和车辆信息填写状态，查看当前处理状态、校验结果或执行进度，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/pass/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 7. `SupplyOrderAPI_SupplyOrderStatusCounter`

**中文说明：** 按状态统计供货申请数量，查看当前处理状态、校验结果或执行进度，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/status/counter`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `SupplyOrderAPI_GetSupplyOrderTimeslots`

**中文说明：** 获取供货时间段，返回指定对象的详细信息，便于后续判断或处理，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/timeslot/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `SupplyOrderAPI_GetSupplyOrderTimeslotStatus`

**中文说明：** 获取供货时间段状态，查看当前处理状态、校验结果或执行进度，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/timeslot/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `SupplyOrderAPI_UpdateSupplyOrderTimeslot`

**中文说明：** 更新供货时间段，根据提交的参数更新已有配置、内容或业务状态，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/timeslot/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 11. `PostingAPI_GetFboPosting`

**中文说明：** 获取FBO 包裹信息，返回指定对象的详细信息，便于后续判断或处理，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbo/get`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 12. `PostingAPI_GetFboPostingList`

**中文说明：** 获取FBO 包裹列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbo/list`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 13. `SupplyOrderGet`

**中文说明：** 获取供货申请信息，返回指定对象的详细信息，便于后续判断或处理，并用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/supply-order/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 14. `SupplyOrderList`

**中文说明：** 获取发往 Ozon 仓库的供货申请列表，用于管理向 Ozon 仓库供货以及查询 FBO 包裹和供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/supply-order/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### FBS 配送

方法数量：**26**

#### 1. `AssemblyCarriagePostingList`

**中文说明：** 获取本次交货中的包裹列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/assembly/carriage/posting/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `AssemblyCarriageProductList`

**中文说明：** 获取本次交货中的商品列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/assembly/carriage/product/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `AssemblyFbsPostingList`

**中文说明：** 获取包裹列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/assembly/fbs/posting/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `AssemblyFbsProductList`

**中文说明：** 获取包裹内商品列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/assembly/fbs/product/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `CarriageAPI_CarriageApprove`

**中文说明：** 确认交货，用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/approve`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `CarriageAPI_CarriageCancel`

**中文说明：** 删除交货批次，对指定对象执行取消、删除、拒绝或归档处理，并用于组织 FBS 交货批次、生成单据标签并完成交货；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/cancel`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 7. `CarriageAPI_CarriageCreate`

**中文说明：** 创建交货批次，根据提交的参数创建新的业务记录，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 8. `CarriageAPI_CarriageDeliveryList`

**中文说明：** 获取配送方式与交货批次列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/delivery/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `CarriageEttnStatus`

**中文说明：** 获取 FBS 可追溯运输电子运单检查状态，用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/ettn/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `CarriageGet`

**中文说明：** 获取运输信息，返回指定对象的详细信息，便于后续判断或处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 11. `CarriageAPI_SetPostings`

**中文说明：** 修改交货批次中的包裹组成，根据提交的参数更新已有配置、内容或业务状态，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/set-postings`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 12. `PostingAPI_GetCarriageAvailableList`

**中文说明：** 获取可用运输批次列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/carriage-available/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 13. `PostingFbsProductTraceableAttribute`

**中文说明：** 获取可追溯商品中未填写的属性列表，用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbs/product/traceable/attribute`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 14. `FbsSplit`

**中文说明：** 将订单拆分为尚未组装的包裹，用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbs/split`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 15. `PostingFbsTraceableSplit`

**中文说明：** 拆分包含可追溯商品的包裹，用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbs/traceable/split`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 16. `CarriageAPI_CarriageDeliveryListV2`

**中文说明：** 获取配送方式与交货批次列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/carriage/delivery/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 17. `PostingAPI_PostingFBSActCheckStatus`

**中文说明：** 获取交货及单据状态，查看当前处理状态、校验结果或执行进度，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/act/check-status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 18. `PostingAPI_PostingFBSActCreate`

**中文说明：** 确认交货并创建单据，根据提交的参数创建新的业务记录，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/act/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 19. `PostingAPI_PostingFBSGetBarcode`

**中文说明：** 获取交货包裹条码，返回指定对象的详细信息，便于后续判断或处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/act/get-barcode`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 20. `PostingAPI_PostingFBSGetBarcodeText`

**中文说明：** 用于交货包裹条码值，具体用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/act/get-barcode/text`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 21. `PostingAPI_PostingFBSActGetContainerLabels`

**中文说明：** 获取货位标签，返回指定对象的详细信息，便于后续判断或处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/act/get-container-labels`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 22. `PostingAPI_PostingFBSGetAct`

**中文说明：** 获取包含单据的 PDF，返回指定对象的详细信息，便于后续判断或处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/act/get-pdf`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 23. `PostingAPI_ActPostingList`

**中文说明：** 获取交货单据中的包裹列表，返回指定对象的详细信息，便于后续判断或处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/act/get-postings`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 24. `PostingAPI_FbsActList`

**中文说明：** 获取交货单据列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/act/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 25. `PostingAPI_PostingFBSDigitalActCheckStatus`

**中文说明：** 获取运单生成状态，查看当前处理状态、校验结果或执行进度，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/digital/act/check-status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 26. `PostingAPI_PostingFBSGetDigitalAct`

**中文说明：** 获取运输交货单，返回指定对象的详细信息，便于后续判断或处理，并用于组织 FBS 交货批次、生成单据标签并完成交货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/digital/act/get-pdf`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### rFBS 配送

方法数量：**7**

#### 1. `PostingAPI_SetPostingCutoff`

**中文说明：** 调整包裹发货日期，根据提交的参数更新已有配置、内容或业务状态，并用于管理由卖家或第三方配送的包裹日期、状态和物流追踪信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/cutoff/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `PostingAPI_PostingTimeslotChangeRestrictions`

**中文说明：** 用于可改期的配送日期，具体用于管理由卖家或第三方配送的包裹日期、状态和物流追踪信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbs/timeslot/change-restrictions`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `PostingAPI_SetPostingTimeslot`

**中文说明：** 用于更改配送日期，具体用于管理由卖家或第三方配送的包裹日期、状态和物流追踪信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbs/timeslot/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `PostingAPI_FbsPostingDelivered`

**中文说明：** 将状态改为“已送达”，用于管理由卖家或第三方配送的包裹日期、状态和物流追踪信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/fbs/posting/delivered`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `PostingAPI_FbsPostingDelivering`

**中文说明：** 将状态改为“配送中”，用于管理由卖家或第三方配送的包裹日期、状态和物流追踪信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/fbs/posting/delivering`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `PostingAPI_FbsPostingLastMile`

**中文说明：** 将状态改为“最后一公里”，用于管理由卖家或第三方配送的包裹日期、状态和物流追踪信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/fbs/posting/last-mile`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `PostingAPI_FbsPostingTrackingNumberSet`

**中文说明：** 添加物流追踪号，根据提交的参数更新已有配置、内容或业务状态，并用于管理由卖家或第三方配送的包裹日期、状态和物流追踪信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/fbs/posting/tracking-number/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 商品上传与更新

方法数量：**20**

#### 1. `ProductAPI_ProductArchive`

**中文说明：** 将商品归档，对指定对象执行取消、删除、拒绝或归档处理，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/archive`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 2. `ProductAPI_ProductUpdateAttributes`

**中文说明：** 更新商品属性，根据提交的参数更新已有配置、内容或业务状态，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/attributes/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `ProductAPI_ImportProductsBySKU`

**中文说明：** 按 SKU 创建商品，将文件或业务数据提交到 Ozon 进行导入和处理，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/import-by-sku`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `ProductAPI_GetImportProductsInfo`

**中文说明：** 查询商品新增或更新状态，返回指定对象的详细信息，便于后续判断或处理，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/import/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `ProductAPI_GetProductInfoDescription`

**中文说明：** 获取商品描述，返回指定对象的详细信息，便于后续判断或处理，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/info/description`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `ProductAPI_GetProductInfoSubscription`

**中文说明：** 用于订阅该商品的用户数量，具体用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/info/subscription`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 7. `ProductAPI_ProductInfoWrongVolume`

**中文说明：** 获取尺寸或重量参数不正确的商品列表，用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/info/wrong-volume`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `ProductAPI_ProductImportPictures`

**中文说明：** 上传或更新商品图片，将文件或业务数据提交到 Ozon 进行导入和处理，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/pictures/import`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 9. `ProductAPI_GetProductPlacementZoneInfo`

**中文说明：** 用于供货前按 SKU 获取商品存放区域，具体用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/placement-zone/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `ProductAPI_GetProductRatingBySku`

**中文说明：** 按 SKU 获取商品内容评分，用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/rating-by-sku`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 11. `ProductAPI_ProductGetRelatedSKU`

**中文说明：** 获取关联 SKU，返回指定对象的详细信息，便于后续判断或处理，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/related-sku/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 12. `ProductAPI_ProductUnarchive`

**中文说明：** 将商品移出归档，用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/unarchive`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 13. `ProductAPI_ProductUpdateOfferID`

**中文说明：** 修改卖家系统中的商品货号，根据提交的参数更新已有配置、内容或业务状态，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/update/offer-id`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 14. `ProductAPI_ProductInfoPicturesV2`

**中文说明：** 获取商品图片，返回指定对象的详细信息，便于后续判断或处理，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/product/pictures/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 15. `ProductAPI_DeleteProducts`

**中文说明：** 从归档中删除没有 SKU 的商品，用于创建、更新和检查 Ozon 商品卡及其内容资料；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/products/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 16. `ProductAPI_ImportProductsV3`

**中文说明：** 创建或更新商品，将文件或业务数据提交到 Ozon 进行导入和处理，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/product/import`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 17. `ProductAPI_GetProductInfoList`

**中文说明：** 按标识符获取商品信息，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/product/info/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 18. `ProductAPI_GetProductList`

**中文说明：** 获取卖家商品目录列表，可按可见性等条件筛选，并返回商品标识、货号和归档状态等基础信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/product/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 19. `ProductAPI_GetProductAttributesV4`

**中文说明：** 获取商品属性说明，返回指定对象的详细信息，便于后续判断或处理，并用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v4/product/info/attributes`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 20. `ProductAPI_GetUploadQuota`

**中文说明：** 用于商品数量、创建及更新限额，具体用于创建、更新和检查 Ozon 商品卡及其内容资料。

- **HTTP 方法：** `POST`
- **接口路径：** `/v4/product/info/limit`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 订单

方法数量：**4**

#### 1. `OrderAPI_OrderCancel`

**中文说明：** 取消指定订单并提交取消原因，用于终止不再继续履约的订单；调用前应确认订单和取消条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/order/cancel`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 2. `OrderAPI_OrderCancelCheck`

**中文说明：** 检查订单是否可以取消，查看当前处理状态、校验结果或执行进度，并用于创建、取消或查询订单取消处理状态；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/order/cancel/check`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 3. `OrderAPI_OrderCancelStatus`

**中文说明：** 获取订单取消状态，查看当前处理状态、校验结果或执行进度，并用于创建、取消或查询订单取消处理状态；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/order/cancel/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `OrderAPI_OrderCreate`

**中文说明：** 根据提交的商品、买家和配送信息创建订单，用于需要通过 API 建立订单记录的业务场景。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/order/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### API 密钥信息

方法数量：**1**

#### 1. `AccessAPI_RolesByToken`

**中文说明：** 获取根据 API 密钥获取角色和可用方法列表，用于确认当前 API 密钥拥有的角色、权限和可调用接口。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/roles`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 卖家后台信息

方法数量：**2**

#### 1. `SellerAPI_SellerInfo`

**中文说明：** 获取当前卖家后台的账户和公司基础信息，并读取订阅类型等数据，用于确认店铺身份与可用能力。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller/info`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 2. `SellerAPI_SellerOzonLogisticsInfo`

**中文说明：** 获取Ozon 配送接入信息，返回指定对象的详细信息，便于后续判断或处理，并用于读取卖家账户、订阅和 Ozon 配送接入情况。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/seller/ozon-logistics/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 发票

方法数量：**4**

#### 1. `invoice_delete`

**中文说明：** 删除发票链接，对指定对象执行取消、删除、拒绝或归档处理，并用于上传、创建、修改或查询订单相关发票；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/invoice/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 2. `invoice_upload`

**中文说明：** 上传发票，将文件或业务数据提交到 Ozon 进行导入和处理，并用于上传、创建、修改或查询订单相关发票。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/invoice/file/upload`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `InvoiceAPI_InvoiceCreateOrUpdateV2`

**中文说明：** 创建或修改发票，根据提交的参数创建新的业务记录，并用于上传、创建、修改或查询订单相关发票。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/invoice/create-or-update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `invoice_getV2`

**中文说明：** 获取发票信息，返回指定对象的详细信息，便于后续判断或处理，并用于上传、创建、修改或查询订单相关发票。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/invoice/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### FBS 与 rFBS 订单处理

方法数量：**21**

#### 1. `PostingAPI_GetPostingFbsCancelReasonV1`

**中文说明：** 获取包裹取消原因，对指定对象执行取消、删除、拒绝或归档处理，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbs/cancel-reason`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 2. `PostingAPI_CreateLabelBatch`

**中文说明：** 创建标签导出任务，根据提交的参数创建新的业务记录，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbs/package-label/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `PostingAPI_GetLabelBatch`

**中文说明：** 获取标签文件，返回指定对象的详细信息，便于后续判断或处理，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbs/package-label/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `PostingAPI_PostingFBSPickupCodeVerify`

**中文说明：** 验证快递员取件码，用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbs/pick-up-code/verify`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `PostingAPI_GetRestrictions`

**中文说明：** 获取收货点限制条件，用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/fbs/restrictions`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `PostingAPI_GetEtgb`

**中文说明：** 用于ETGB 海关申报单，具体用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/global/etgb`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 7. `PostingAPI_UnpaidLegalProductList`

**中文说明：** 获取法人客户已下单但未付款的商品列表，用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/unpaid-legal/product/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `PostingAPI_MoveFbsPostingToArbitration`

**中文说明：** 用于对包裹发起争议，具体用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/arbitration`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 9. `PostingAPI_MoveFbsPostingToAwaitingDelivery`

**中文说明：** 将包裹转入待交货状态，用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/awaiting-delivery`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 10. `PostingAPI_CancelFbsPosting`

**中文说明：** 取消包裹，对指定对象执行取消、删除、拒绝或归档处理，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/cancel`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 11. `PostingAPI_GetPostingFbsCancelReasonList`

**中文说明：** 获取包裹取消原因列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/cancel-reason/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 12. `PostingAPI_GetFbsPostingByBarcode`

**中文说明：** 按条码获取包裹信息，返回指定对象的详细信息，便于后续判断或处理，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/get-by-barcode`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 13. `PostingAPI_PostingFBSPackageLabel`

**中文说明：** 打印标签，用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/package-label`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 14. `PostingAPI_CreateLabelBatchV2`

**中文说明：** 创建标签生成任务，根据提交的参数创建新的业务记录，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/package-label/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 15. `PostingAPI_CancelFbsPostingProduct`

**中文说明：** 取消包裹内部分商品的发货，对指定对象执行取消、删除、拒绝或归档处理，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/product/cancel`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 16. `PostingAPI_ListCountryProductFbsPostingV2`

**中文说明：** 获取可用生产国列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/product/country/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 17. `PostingAPI_SetCountryProductFbsPostingV2`

**中文说明：** 添加商品生产国信息，根据提交的参数更新已有配置、内容或业务状态，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/posting/fbs/product/country/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 18. `PostingAPI_GetFbsPostingV3`

**中文说明：** 按标识符获取包裹信息，返回指定对象的详细信息，便于后续判断或处理，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/posting/fbs/get`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 19. `PostingAPI_GetFbsPostingListV3`

**中文说明：** 获取包裹列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/posting/fbs/list`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 20. `PostingAPI_GetFbsPostingUnfulfilledList`

**中文说明：** 获取未处理包裹列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/posting/fbs/unfulfilled/list`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 21. `PostingAPI_PostingMultiBoxQtySetV3`

**中文说明：** 设置多箱包裹的箱数，根据提交的参数更新已有配置、内容或业务状态，并用于完成 FBS/rFBS 包裹查询、打单、发货、取消和异常处理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/posting/multiboxqty/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 订单取消

方法数量：**3**

#### 1. `CancellationAPI_ConditionalCancellationApproveV2`

**中文说明：** 批准 rFBS 取消申请，用于审核和处理 rFBS 买家的条件取消申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/conditional-cancellation/approve`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `CancellationAPI_GetConditionalCancellationListV2`

**中文说明：** 获取 rFBS 取消申请列表，用于审核和处理 rFBS 买家的条件取消申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/conditional-cancellation/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `CancellationAPI_ConditionalCancellationRejectV2`

**中文说明：** 拒绝 rFBS 取消申请，对指定对象执行取消、删除、拒绝或归档处理，并用于审核和处理 rFBS 买家的条件取消申请；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/conditional-cancellation/reject`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

### 包裹

方法数量：**3**

#### 1. `PostingAPI_PostingCancel`

**中文说明：** 取消订单中的包裹，对指定对象执行取消、删除、拒绝或归档处理，并用于处理订单中的包裹取消、状态和商品标识信息；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/cancel`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 2. `PostingAPI_PostingCancelStatus`

**中文说明：** 检查包裹取消状态，查看当前处理状态、校验结果或执行进度，并用于处理订单中的包裹取消、状态和商品标识信息；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/cancel/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `PostingAPI_PostingMarks`

**中文说明：** 获取包裹内商品实例的标识码，用于处理订单中的包裹取消、状态和商品标识信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/marks`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 报告

方法数量：**11**

#### 1. `FinanceAPI_FinanceCashFlowStatementList`

**中文说明：** 获取指定期间的资金流水或现金流报告，用于核对收入、支出、退款、佣金及其他财务变动。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/finance/cash-flow-statement/list`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 2. `ReportAPI_CreateDiscountedReport`

**中文说明：** 获取折价商品报告，根据提交的参数创建新的业务记录，并用于创建经营报告并查询报告生成状态或下载结果。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/report/discounted/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `ReportAPI_ReportInfo`

**中文说明：** 查询指定异步报告任务的当前状态和结果信息，用于判断报告是否已经生成并可以下载。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/report/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `ReportAPI_ReportList`

**中文说明：** 获取卖家已经创建的报告任务列表，用于查看报告类型、生成状态和历史记录。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/report/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `CreateCompanyMarkedProductsSalesReport`

**中文说明：** 生成带标识商品销售报告，根据提交的参数创建新的业务记录，并用于创建经营报告并查询报告生成状态或下载结果。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/report/marked-products-sales/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `CreatePlacementByProductsReport`

**中文说明：** 获取按商品统计的仓储费用报告，用于创建经营报告并查询报告生成状态或下载结果。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/report/placement/by-products/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `CreatePlacementBySuppliesReport`

**中文说明：** 获取按供货批次统计的仓储费用报告，用于创建经营报告并查询报告生成状态或下载结果。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/report/placement/by-supplies/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 8. `ReportAPI_CreateCompanyPostingsReport`

**中文说明：** 获取包裹报告，根据提交的参数创建新的业务记录，并用于创建经营报告并查询报告生成状态或下载结果。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/report/postings/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 9. `ReportAPI_CreateCompanyProductsReport`

**中文说明：** 获取商品报告，根据提交的参数创建新的业务记录，并用于创建经营报告并查询报告生成状态或下载结果。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/report/products/create`
- **安全级别：** 写入
- **订阅要求：** PREMIUM

---

#### 10. `ReportAPI_CreateStockByWarehouseReport`

**中文说明：** 获取FBS 仓库库存报告，生成、查询或下载相应的统计与经营报告，并用于创建经营报告并查询报告生成状态或下载结果。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/report/warehouse/stock`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 11. `ReportAPI_ReportReturnsCreate`

**中文说明：** 获取退货报告，根据提交的参数创建新的业务记录，并用于创建经营报告并查询报告生成状态或下载结果。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/report/returns/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 配送区域

方法数量：**7**

#### 1. `PolygonAPI_BindPolygon`

**中文说明：** 将配送方式绑定到配送区域，用于配置配送范围、区域坐标和配送时间。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/polygon/bind`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `PolygonAPI_CreatePolygon`

**中文说明：** 创建配送区域，根据提交的参数创建新的业务记录，并用于配置配送范围、区域坐标和配送时间。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/polygon/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `PolygonDelete`

**中文说明：** 从配送范围中删除配送区域，对指定对象执行取消、删除、拒绝或归档处理，并用于配置配送范围、区域坐标和配送时间；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/polygon/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 4. `PolygonList`

**中文说明：** 获取配送方式已配置的配送区域列表，用于配置配送范围、区域坐标和配送时间。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/polygon/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `PolygonTimeCoordinatesUpdate`

**中文说明：** 更新配送区域坐标，根据提交的参数更新已有配置、内容或业务状态，并用于配置配送范围、区域坐标和配送时间。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/polygon/time/coordinates/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `PolygonTimeSet`

**中文说明：** 设置配送区域的新配送时效，根据提交的参数更新已有配置、内容或业务状态，并用于配置配送范围、区域坐标和配送时间。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/polygon/time/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `PolygonBind`

**中文说明：** 将配送方式绑定到配送区域，用于配置配送范围、区域坐标和配送时间。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/polygon/bind`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 取消原因

方法数量：**3**

#### 1. `CancelReasonList`

**中文说明：** 获取包裹取消原因，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于获取 Ozon 允许使用的订单或包裹取消原因；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cancel-reason/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `CancelReasonListByOrder`

**中文说明：** 获取订单取消原因，对指定对象执行取消、删除、拒绝或归档处理，并用于获取 Ozon 允许使用的订单或包裹取消原因；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cancel-reason/list-by-order`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `CancelReasonAPI_CancelReasonListByPosting`

**中文说明：** 获取包裹取消原因，对指定对象执行取消、删除、拒绝或归档处理，并用于获取 Ozon 允许使用的订单或包裹取消原因；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cancel-reason/list-by-posting`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 通行证

方法数量：**7**

#### 1. `carriagePassCreate`

**中文说明：** 创建通行证，根据提交的参数创建新的业务记录，并用于管理车辆、人员进出仓库或领取退货所需的通行证。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/pass/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `carriagePassDelete`

**中文说明：** 删除通行证，对指定对象执行取消、删除、拒绝或归档处理，并用于管理车辆、人员进出仓库或领取退货所需的通行证；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/pass/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 3. `carriagePassUpdate`

**中文说明：** 更新通行证，根据提交的参数更新已有配置、内容或业务状态，并用于管理车辆、人员进出仓库或领取退货所需的通行证。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/pass/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `PassList`

**中文说明：** 获取通行证列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于管理车辆、人员进出仓库或领取退货所需的通行证。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pass/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `returnPassCreate`

**中文说明：** 创建退货通行证，根据提交的参数创建新的业务记录，并用于管理车辆、人员进出仓库或领取退货所需的通行证。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/return/pass/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `returnPassDelete`

**中文说明：** 删除退货通行证，对指定对象执行取消、删除、拒绝或归档处理，并用于管理车辆、人员进出仓库或领取退货所需的通行证；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/return/pass/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 7. `returnPassUpdate`

**中文说明：** 更新退货通行证，根据提交的参数更新已有配置、内容或业务状态，并用于管理车辆、人员进出仓库或领取退货所需的通行证。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/return/pass/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 其他方法

方法数量：**13**

#### 1. `AnalyticsAPI_ManageStocks`

**中文说明：** 用于库存管理，具体用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/analytics/manage/stocks`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `CarriageActDiscrepancyPDF`

**中文说明：** 获取 FBS 交货差异单，用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/carriage/act-discrepancy/pdf`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `GetFinanceBalanceV1`

**中文说明：** 获取余额报告，用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/finance/balance`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `ProductAPI_GetProductStairwayDiscountByQuantity`

**中文说明：** 获取阶梯数量折扣信息，返回指定对象的详细信息，便于后续判断或处理，并用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/stairway-discount/by-quantity/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `ProductAPI_SetProductStairwayDiscountByQuantity`

**中文说明：** 管理阶梯数量折扣，根据提交的参数更新已有配置、内容或业务状态，并用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/stairway-discount/by-quantity/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `ProductVisibilitySet`

**中文说明：** 设置商品在 Ozon 和 Ozon Select 店铺前台的可见性，用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/visibility/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `GetSupplierReturnsSummaryReport`

**中文说明：** 获取FBO 库存提货与销毁报告，用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/removal/from-stock/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `GetSupplyReturnsSummaryReport`

**中文说明：** 获取FBO 供货批次提货与销毁报告，用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/removal/from-supply/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `WarehouseOZONList`

**中文说明：** 获取 Ozon 仓库列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/ozon/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `WarehouseRfbsPause`

**中文说明：** 用于暂停 rFBS 仓库，具体用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/rfbs/pause`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 11. `WarehouseRfbsUnpause`

**中文说明：** 恢复 rFBS 仓库，用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/rfbs/unpause`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 12. `GetDiscountTaskListV2`

**中文说明：** 获取折扣申请列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/actions/discounts-task/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 13. `DraftClusterList`

**中文说明：** 获取大区集群信息，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于完成对应的库存、财务、折扣、仓库或商品辅助管理任务。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/cluster/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### FBP 直送供货管理

方法数量：**4**

#### 1. `FbpAPI_FbpOrderDirectCancel`

**中文说明：** 取消直送供货，对指定对象执行取消、删除、拒绝或归档处理，并用于管理已创建的 FBP 直送供货、配送信息和供货时间段；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/direct/cancel`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 2. `FbpAPI_FbpOrderDirectSellerDlvEdit`

**中文说明：** 更新卖家自行配送信息，根据提交的参数更新已有配置、内容或业务状态，并用于管理已创建的 FBP 直送供货、配送信息和供货时间段。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/direct/seller-dlv/edit`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `FbpAPI_FbpEditTimeslot`

**中文说明：** 编辑供货申请中的时间段，根据提交的参数更新已有配置、内容或业务状态，并用于管理已创建的 FBP 直送供货、配送信息和供货时间段。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/direct/timeslot/edit`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `FbpAPI_FbpAvailableTimeslotList`

**中文说明：** 获取供货时间段列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于管理已创建的 FBP 直送供货、配送信息和供货时间段。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/direct/timeslot/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### FBP 送至交接点供货管理

方法数量：**3**

#### 1. `FbpAPI_FbpOrderDropOffCancel`

**中文说明：** 取消送至交接点的供货，对指定对象执行取消、删除、拒绝或归档处理，并用于管理送至 drop-off 交接点的 FBP 供货；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/drop-off/cancel`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 2. `FbpAPI_FbpOrderDropOffDlvEdit`

**中文说明：** 编辑送至交接点的供货信息，根据提交的参数更新已有配置、内容或业务状态，并用于管理送至 drop-off 交接点的 FBP 供货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/drop-off/dlv/edit`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `FbpAPI_FbpOrderDropOffTimetable`

**中文说明：** 获取交接点营业时间，用于管理送至 drop-off 交接点的 FBP 供货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/drop-off/timetable`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### FBP 上门取件供货管理

方法数量：**2**

#### 1. `FbpAPI_FbpOrderPickUpCancel`

**中文说明：** 取消上门取件供货，对指定对象执行取消、删除、拒绝或归档处理，并用于管理由承运方上门取件的 FBP 供货；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/pick-up/cancel`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 2. `FbpAPI_FbpOrderPickUpDlvEdit`

**中文说明：** 修改取货点信息，根据提交的参数更新已有配置、内容或业务状态，并用于管理由承运方上门取件的 FBP 供货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/pick-up/dlv/edit`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### FBP 供货草稿管理

方法数量：**3**

#### 1. `FbpAPI_FbpDraftGet`

**中文说明：** 获取供货草稿信息，返回指定对象的详细信息，便于后续判断或处理，并用于查询 FBP 供货草稿和可用合作仓库。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `FbpAPI_FbpDraftList`

**中文说明：** 获取供货草稿列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询 FBP 供货草稿和可用合作仓库。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `FbpWarehouseList`

**中文说明：** 获取合作仓库列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询 FBP 供货草稿和可用合作仓库。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/warehouse/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### FBP 送至交接点供货草稿管理

方法数量：**8**

#### 1. `FbpDraftDropOffCreate`

**中文说明：** 创建送至交接点的供货草稿，根据提交的参数创建新的业务记录，并用于创建并维护送至 drop-off 交接点的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/drop-off/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `FbpDraftDropOffDelete`

**中文说明：** 删除送至交接点的供货草稿，对指定对象执行取消、删除、拒绝或归档处理，并用于创建并维护送至 drop-off 交接点的 FBP 供货草稿；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/drop-off/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 3. `FbpDraftDropOffDlvEdit`

**中文说明：** 编辑交接点供货草稿的配送详情，用于创建并维护送至 drop-off 交接点的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/drop-off/dlv/edit`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `FbpDraftDropOffPointList`

**中文说明：** 获取省内交接点列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建并维护送至 drop-off 交接点的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/drop-off/point/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `FbpDraftDropOffPointTimetable`

**中文说明：** 获取交接点营业时间表，用于创建并维护送至 drop-off 交接点的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/drop-off/point/timetable`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `FbpDraftDropOffProductValidate`

**中文说明：** 检查合作仓库可接收的商品列表，用于创建并维护送至 drop-off 交接点的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/drop-off/product/validate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `FbpDraftDropOffProvinceList`

**中文说明：** 获取省份列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建并维护送至 drop-off 交接点的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/drop-off/province/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `FbpDraftDropOffRegistrate`

**中文说明：** 将草稿转为正式供货，根据提交的参数创建新的业务记录，并用于创建并维护送至 drop-off 交接点的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/drop-off/registrate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### FBP 直送供货草稿管理

方法数量：**10**

#### 1. `FbpDraftDirectCreate`

**中文说明：** 创建未指定配送方式的供货申请草稿，用于创建并维护直送或第三方运输的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/direct/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `FbpDraftDirectDelete`

**中文说明：** 删除供货申请草稿，对指定对象执行取消、删除、拒绝或归档处理，并用于创建并维护直送或第三方运输的 FBP 供货草稿；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/direct/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 3. `FbpDraftDirectProductValidate`

**中文说明：** 检查合作仓库商品列表，用于创建并维护直送或第三方运输的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/direct/product/validate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `FbpDraftDirectRegistrate`

**中文说明：** 将草稿转为正式供货，根据提交的参数创建新的业务记录，并用于创建并维护直送或第三方运输的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/direct/registrate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `FbpDraftDirectSellerDlvCreate`

**中文说明：** 创建卖家自行配送的供货草稿，用于创建并维护直送或第三方运输的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/direct/seller-dlv/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `FbpDraftDirectSellerDlvEdit`

**中文说明：** 更新草稿中的卖家自行配送信息，用于创建并维护直送或第三方运输的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/direct/seller-dlv/edit`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `FbpDraftDirectTimeslotEdit`

**中文说明：** 编辑草稿中的供货时间段，根据提交的参数更新已有配置、内容或业务状态，并用于创建并维护直送或第三方运输的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/direct/timeslot/edit`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 8. `FbpDraftDirectGetTimeslot`

**中文说明：** 获取直送供货时间段列表，返回指定对象的详细信息，便于后续判断或处理，并用于创建并维护直送或第三方运输的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/direct/timeslot/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `FbpAPI_FbpDraftDirectTplDlvCreate`

**中文说明：** 创建第三方运输公司配送申请草稿，用于创建并维护直送或第三方运输的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/direct/tpl-dlv/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 10. `FbpAPI_FbpDraftDirectTplDlvEdit`

**中文说明：** 编辑第三方运输公司配送方式的供货草稿，用于创建并维护直送或第三方运输的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/direct/tpl-dlv/edit`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### FBP 上门取件供货草稿管理

方法数量：**5**

#### 1. `FbpAPI_FbpDraftPickupCreate`

**中文说明：** 创建上门取件供货申请草稿，根据提交的参数创建新的业务记录，并用于创建并维护上门取件方式的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/pick-up/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `FbpAPI_FbpDraftPickUpDelete`

**中文说明：** 取消上门取件供货申请草稿，对指定对象执行取消、删除、拒绝或归档处理，并用于创建并维护上门取件方式的 FBP 供货草稿；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/pick-up/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 3. `FbpAPI_FbpDraftPickupDlvEdit`

**中文说明：** 修改上门取件供货申请草稿，根据提交的参数更新已有配置、内容或业务状态，并用于创建并维护上门取件方式的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/pick-up/dlv/edit`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `FbpAPI_FbpDraftPickUpProductValidate`

**中文说明：** 校验上门取件供货的商品列表，用于创建并维护上门取件方式的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/pick-up/product/validate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `FbpDraftPickUpRegistrate`

**中文说明：** 将草稿转为正式供货，根据提交的参数创建新的业务记录，并用于创建并维护上门取件方式的 FBP 供货草稿。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/draft/pick-up/registrate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 问答管理

方法数量：**8**

#### 1. `QuestionAnswer_Create`

**中文说明：** 创建问题回复，根据提交的参数创建新的业务记录，并用于查看买家商品问题、回复问题并管理问题状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/question/answer/create`
- **安全级别：** 写入
- **订阅要求：** PREMIUM_PLUS

---

#### 2. `QuestionAnswer_Delete`

**中文说明：** 删除问题回复，对指定对象执行取消、删除、拒绝或归档处理，并用于查看买家商品问题、回复问题并管理问题状态；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/question/answer/delete`
- **安全级别：** 破坏性
- **订阅要求：** PREMIUM_PLUS

---

#### 3. `QuestionAnswer_List`

**中文说明：** 获取问题回复列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查看买家商品问题、回复问题并管理问题状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/question/answer/list`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PLUS

---

#### 4. `Question_ChangeStatus`

**中文说明：** 修改问题状态，根据提交的参数更新已有配置、内容或业务状态，并用于查看买家商品问题、回复问题并管理问题状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/question/change-status`
- **安全级别：** 写入
- **订阅要求：** PREMIUM_PLUS

---

#### 5. `Question_Count`

**中文说明：** 按状态统计问题数量，用于查看买家商品问题、回复问题并管理问题状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/question/count`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PLUS

---

#### 6. `Question_Info`

**中文说明：** 获取问题信息，返回指定对象的详细信息，便于后续判断或处理，并用于查看买家商品问题、回复问题并管理问题状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/question/info`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PLUS

---

#### 7. `Question_List`

**中文说明：** 获取问题列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查看买家商品问题、回复问题并管理问题状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/question/list`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PLUS

---

#### 8. `Question_TopSku`

**中文说明：** 用于问题数量最多的商品，具体用于查看买家商品问题、回复问题并管理问题状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/question/top-sku`
- **安全级别：** 写入
- **订阅要求：** PREMIUM_PLUS

---

### 经济型商品管理

方法数量：**2**

#### 1. `QuantGetInfo`

**中文说明：** 获取经济型商品信息，返回指定对象的详细信息，便于后续判断或处理，并用于查询 Ozon 经济型商品及其销售单位信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/quant/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `QuantProductList`

**中文说明：** 获取经济型商品列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询 Ozon 经济型商品及其销售单位信息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/quant/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 评价管理

方法数量：**7**

#### 1. `ReviewAPI_ReviewChangeStatus`

**中文说明：** 修改评价状态，根据提交的参数更新已有配置、内容或业务状态，并用于查询买家评价、回复评价并管理评价处理状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/review/change-status`
- **安全级别：** 写入
- **订阅要求：** PREMIUM_PRO

---

#### 2. `ReviewAPI_CommentCreate`

**中文说明：** 回复评价，根据提交的参数创建新的业务记录，并用于查询买家评价、回复评价并管理评价处理状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/review/comment/create`
- **安全级别：** 写入
- **订阅要求：** PREMIUM_PRO

---

#### 3. `ReviewAPI_CommentDelete`

**中文说明：** 删除评价回复，对指定对象执行取消、删除、拒绝或归档处理，并用于查询买家评价、回复评价并管理评价处理状态；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/review/comment/delete`
- **安全级别：** 破坏性
- **订阅要求：** PREMIUM_PRO

---

#### 4. `ReviewAPI_CommentList`

**中文说明：** 获取评价回复列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询买家评价、回复评价并管理评价处理状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/review/comment/list`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PRO

---

#### 5. `ReviewAPI_ReviewCount`

**中文说明：** 按状态统计评价数量，用于查询买家评价、回复评价并管理评价处理状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/review/count`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PRO

---

#### 6. `ReviewAPI_ReviewInfo`

**中文说明：** 获取评价信息，返回指定对象的详细信息，便于后续判断或处理，并用于查询买家评价、回复评价并管理评价处理状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/review/info`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PRO

---

#### 7. `ReviewAPI_ReviewList`

**中文说明：** 获取评价列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询买家评价、回复评价并管理评价处理状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/review/list`
- **安全级别：** 只读
- **订阅要求：** PREMIUM_PRO

---

### 推送通知管理

方法数量：**7**

#### 1. `CheckNotification`

**中文说明：** 检查通知回调地址，查看当前处理状态、校验结果或执行进度，并用于配置 Ozon 事件通知的回调地址和通知类型。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/notification/check`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `DeleteNotification`

**中文说明：** 删除通知回调地址，对指定对象执行取消、删除、拒绝或归档处理，并用于配置 Ozon 事件通知的回调地址和通知类型；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/notification/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 3. `EnableNotification`

**中文说明：** 启用或停用通知回调，用于配置 Ozon 事件通知的回调地址和通知类型。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/notification/enable`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `NotificationList`

**中文说明：** 获取已接入通知回调地址的信息，用于配置 Ozon 事件通知的回调地址和通知类型。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/notification/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `GetNotificationPushTypeList`

**中文说明：** 获取推送通知类型，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于配置 Ozon 事件通知的回调地址和通知类型。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/notification/push-type/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `SetNotification`

**中文说明：** 用于接入通知回调地址，具体用于配置 Ozon 事件通知的回调地址和通知类型。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/notification/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `UpdateNotification`

**中文说明：** 修改通知回调地址，根据提交的参数更新已有配置、内容或业务状态，并用于配置 Ozon 事件通知的回调地址和通知类型。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/notification/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 已创建 FBP 供货管理

方法数量：**10**

#### 1. `FbpAPI_FbpCreateAct`

**中文说明：** 生成收货验收单，根据提交的参数创建新的业务记录，并用于查询正式 FBP 供货并生成验收单、运输单据和标签。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/act-from/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `FbpAPI_FbpCheckActState`

**中文说明：** 获取收货验收单生成状态，返回指定对象的详细信息，便于后续判断或处理，并用于查询正式 FBP 供货并生成验收单、运输单据和标签。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/act-from/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `FbpAPI_FbpCreateConsignmentNote`

**中文说明：** 生成运输单据，根据提交的参数创建新的业务记录，并用于查询正式 FBP 供货并生成验收单、运输单据和标签。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/act-to/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `FbpAPI_FbpCheckConsignmentNoteState`

**中文说明：** 获取运输单据生成状态，返回指定对象的详细信息，便于后续判断或处理，并用于查询正式 FBP 供货并生成验收单、运输单据和标签。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/act-to/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `FbpAPI_FbpArchiveGet`

**中文说明：** 获取已完成供货信息，返回指定对象的详细信息，便于后续判断或处理，并用于查询正式 FBP 供货并生成验收单、运输单据和标签。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/archive/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `FbpAPI_FbpArchiveList`

**中文说明：** 获取已完成供货列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询正式 FBP 供货并生成验收单、运输单据和标签。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/archive/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 7. `FbpAPI_FbpCreateLabel`

**中文说明：** 创建标签生成任务，根据提交的参数创建新的业务记录，并用于查询正式 FBP 供货并生成验收单、运输单据和标签。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/label/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 8. `FbpAPI_FbpGetLabel`

**中文说明：** 获取标签生成任务状态，返回指定对象的详细信息，便于后续判断或处理，并用于查询正式 FBP 供货并生成验收单、运输单据和标签。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/label/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `FbpAPI_FbpOrderGet`

**中文说明：** 获取指定供货信息，返回指定对象的详细信息，便于后续判断或处理，并用于查询正式 FBP 供货并生成验收单、运输单据和标签。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `FbpAPI_FbpOrderList`

**中文说明：** 获取供货列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询正式 FBP 供货并生成验收单、运输单据和标签。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbp/order/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 数字商品管理

方法数量：**3**

#### 1. `UploadPostingCodes`

**中文说明：** 上传包裹中的数字商品兑换码，用于管理数字商品兑换码、包裹和可售库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/digital/codes/upload`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `ListPostingCodes`

**中文说明：** 获取包裹列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于管理数字商品兑换码、包裹和可售库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/posting/digital/list`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 3. `DigitalProductAPI_StocksImport`

**中文说明：** 更新数字商品库存数量，将文件或业务数据提交到 Ozon 进行导入和处理，并用于管理数字商品兑换码、包裹和可售库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/digital/stocks/import`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### FBS 与 rFBS 仓库管理

方法数量：**10**

#### 1. `WarehouseAPI_DeliveryMethodList`

**中文说明：** 获取仓库配送方式列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询和维护卖家 FBS/rFBS 仓库、配送方式及退货设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/delivery-method/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `GetDeliveryMethodReturnSettingsV1`

**中文说明：** 获取 rFBS 与 rFBS Express 退货设置，用于查询和维护卖家 FBS/rFBS 仓库、配送方式及退货设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/delivery-method/return/settings/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `ArchiveWarehouseFBS`

**中文说明：** 将仓库归档，对指定对象执行取消、删除、拒绝或归档处理，并用于查询和维护卖家 FBS/rFBS 仓库、配送方式及退货设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/archive`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 4. `WarehouseInvalidProductsGet`

**中文说明：** 获取配送受限商品列表，返回指定对象的详细信息，便于后续判断或处理，并用于查询和维护卖家 FBS/rFBS 仓库、配送方式及退货设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/invalid-products/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `WarehouseAPI_WarehouseList`

**中文说明：** 获取卖家已配置的 FBS/rFBS 仓库列表及基础状态，用于选择仓库、检查配置和后续库存或配送管理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `GetWarehouseFBSOperationStatus`

**中文说明：** 获取操作状态，查看当前处理状态、校验结果或执行进度，并用于查询和维护卖家 FBS/rFBS 仓库、配送方式及退货设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/operation/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 7. `UnarchiveWarehouseFBS`

**中文说明：** 将仓库移出归档，用于查询和维护卖家 FBS/rFBS 仓库、配送方式及退货设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/unarchive`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 8. `WarehouseWithInvalidProducts`

**中文说明：** 获取含配送受限商品的仓库列表，用于查询和维护卖家 FBS/rFBS 仓库、配送方式及退货设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/warehouses-with-invalid-products`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 9. `WarehouseAPI_DeliveryMethodListV2`

**中文说明：** 获取realFBS 仓库配送方式列表，用于查询和维护卖家 FBS/rFBS 仓库、配送方式及退货设置。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/delivery-method/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `WarehouseListV2`

**中文说明：** 获取新版卖家仓库列表及相关配置数据，用于查看仓库状态、配送模式和后续仓库管理。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/warehouse/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 卖家评分

方法数量：**4**

#### 1. `RatingAPI_RatingHistoryV1`

**中文说明：** 获取指定时期内的卖家评分信息，用于监控卖家评分、履约质量和影响评分的异常包裹。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/rating/history`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 2. `RatingAPI_GetFBSRatingIndexInfoV1`

**中文说明：** 获取 FBS 和 rFBS 错误指数，用于监控卖家评分、履约质量和影响评分的异常包裹。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/rating/index/fbs/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `RatingAPI_ListFBSRatingIndexPostingsV1`

**中文说明：** 获取影响 FBS 和 rFBS 错误指数的包裹列表，用于监控卖家评分、履约质量和影响评分的异常包裹。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/rating/index/fbs/posting/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `RatingAPI_RatingSummaryV1`

**中文说明：** 获取卖家当前评分信息，用于监控卖家评分、履约质量和影响评分的异常包裹。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/rating/summary`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

### 品牌认证

方法数量：**1**

#### 1. `BrandAPI_BrandCompanyCertificationList`

**中文说明：** 获取可认证品牌列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询可以向 Ozon 提交品牌认证的品牌范围。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/brand/company-certification/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 质量证书

方法数量：**15**

#### 1. `ProductAPI_ProductCertificateAccordanceTypes`

**中文说明：** 用于合规类型列表（版本 1），具体用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `GET`
- **接口路径：** `/v1/product/certificate/accordance-types`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `ProductAPI_ProductCertificateBind`

**中文说明：** 将证书绑定到商品，用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certificate/bind`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `ProductAPI_ProductCertificateCreate`

**中文说明：** 为商品添加证书，根据提交的参数创建新的业务记录，并用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certificate/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `CertificateDelete`

**中文说明：** 删除证书，对指定对象执行取消、删除、拒绝或归档处理，并用于创建、绑定、查询和维护商品质量或合规证书；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certificate/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 5. `CertificateInfo`

**中文说明：** 获取证书信息，返回指定对象的详细信息，便于后续判断或处理，并用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certificate/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `CertificateList`

**中文说明：** 获取证书列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certificate/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 7. `ProductStatusList`

**中文说明：** 获取商品可用状态列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certificate/product_status/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `CertificateProductsList`

**中文说明：** 获取已绑定证书的商品列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certificate/products/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `RejectionReasonsList`

**中文说明：** 获取证书可能被拒绝的原因，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建、绑定、查询和维护商品质量或合规证书；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certificate/rejection_reasons/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `CertificateStatusList`

**中文说明：** 获取证书可用状态列表，查看当前处理状态、校验结果或执行进度，并用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certificate/status/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 11. `ProductAPI_ProductCertificateTypes`

**中文说明：** 获取文件类型字典，用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `GET`
- **接口路径：** `/v1/product/certificate/types`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 12. `CertificateUnbind`

**中文说明：** 用于解除商品与证书的绑定，具体用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certificate/unbind`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 13. `ProductAPI_V1ProductCertificationList`

**中文说明：** 获取需要认证的类目列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/certification/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 14. `CertificateAccordanceTypes`

**中文说明：** 用于合规类型列表（版本 2），具体用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `GET`
- **接口路径：** `/v2/product/certificate/accordance-types/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 15. `ProductAPI_ProductCertificationList`

**中文说明：** 获取需要认证的类目列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建、绑定、查询和维护商品质量或合规证书。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/product/certification/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### FBS 仓库创建与管理

方法数量：**17**

#### 1. `WarehouseAPI_CreateWarehouseFBS`

**中文说明：** 创建仓库，根据提交的参数创建新的业务记录，并用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `WarehouseAPI_ListDropOffPointsForCreateFBSWarehouse`

**中文说明：** 获取创建仓库可用的交接点列表，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/create/drop-off/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `WarehouseFbsCreateDropOffTimeslotList`

**中文说明：** 获取创建交接点交货仓库可用的时间段，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/create/drop-off/timeslot/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `WarehouseFbsCreatePickUpTimeslotList`

**中文说明：** 获取创建上门取件仓库可用的时间段，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/create/pick-up/timeslot/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `WarehouseFBSCreateReturnPointList`

**中文说明：** 获取创建仓库可用的退货点列表，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/create/return-point/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `UpdateWarehouseFBSFirstMile`

**中文说明：** 更新首公里配送设置，根据提交的参数更新已有配置、内容或业务状态，并用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/first-mile/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `WarehouseFbsPickUpCourierCancel`

**中文说明：** 取消上门取件交货的快递员预约，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/pickup/courier/cancel`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 8. `WarehouseFbsPickUpCourierCreate`

**中文说明：** 创建上门取件交货的快递员预约，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/pickup/courier/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 9. `WarehouseFbsPickUpHistoryList`

**中文说明：** 获取向快递员交货的历史记录，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/pickup/history/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `WarehouseFbsPickUpPlanningList`

**中文说明：** 获取可安排快递员交货的仓库列表，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/pickup/planning/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 11. `WarehouseFbsReturnMileCheck`

**中文说明：** 检查仓库是否需要设置退货线路，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/return-mile/check`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 12. `WarehouseFBSReturnMileInfo`

**中文说明：** 获取退货线路信息，返回指定对象的详细信息，便于后续判断或处理，并用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/return-mile/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 13. `UpdateWarehouseFBS`

**中文说明：** 更新仓库，根据提交的参数更新已有配置、内容或业务状态，并用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 14. `WarehouseAPI_ListDropOffPointsForUpdateFBSWarehouse`

**中文说明：** 获取修改仓库信息可用的交接点列表，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/update/drop-off/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 15. `WarehouseFbsUpdateDropOffTimeslotList`

**中文说明：** 获取更新交接点交货仓库可用的时间段，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/update/drop-off/timeslot/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 16. `WarehouseFbsUpdatePickUpTimeslotList`

**中文说明：** 获取更新上门取件仓库可用的时间段，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/update/pick-up/timeslot/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 17. `WarehouseFBSUpdateReturnPointList`

**中文说明：** 获取更新仓库可用的退货点列表，用于创建或更新 FBS 仓库及其交接点、时间段和退货线路。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbs/update/return-point/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### FBO 供货申请创建与管理

方法数量：**30**

#### 1. `CargoesAPI_CargoesLabelCreate`

**中文说明：** 生成货运单元标签，根据提交的参数创建新的业务记录，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cargoes-label/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `CargoesAPI_CargoesLabelFile`

**中文说明：** 获取货运单元标签 PDF，用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `GET`
- **接口路径：** `/v1/cargoes-label/file/{file_guid}`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `CargoesAPI_CargoesLabelGet`

**中文说明：** 获取货运单元标签标识符，返回指定对象的详细信息，便于后续判断或处理，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cargoes-label/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `CargoesAPI_CargoesCreate`

**中文说明：** 设置货运单元，根据提交的参数创建新的业务记录，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cargoes/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `CargoesAPI_CargoesCreateInfo`

**中文说明：** 获取设置货运单元的处理信息，用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cargoes/create/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `CargoesAPI_CargoesDelete`

**中文说明：** 删除供货申请中的货运单元，对指定对象执行取消、删除、拒绝或归档处理，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cargoes/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 7. `CargoesAPI_CargoesDeleteStatus`

**中文说明：** 获取货运单元删除状态，查看当前处理状态、校验结果或执行进度，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cargoes/delete/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `CargoesGet`

**中文说明：** 获取货运单元信息，返回指定对象的详细信息，便于后续判断或处理，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cargoes/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `CargoesAPI_CargoesRulesGet`

**中文说明：** 用于FBO 货运单元设置检查清单，具体用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cargoes/rules/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `SupplyDraftAPI_DraftClusterList`

**中文说明：** 获取集群及其仓库信息，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/cluster/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 11. `SupplyDraftAPI_DraftCreate`

**中文说明：** 创建供货申请草稿，根据提交的参数创建新的业务记录，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/draft/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 12. `SupplyDraftAPI_DraftCreateInfo`

**中文说明：** 获取供货申请草稿信息，返回指定对象的详细信息，便于后续判断或处理，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/draft/create/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 13. `DraftCrossdockCreate`

**中文说明：** 创建交叉转运供货申请草稿，根据提交的参数创建新的业务记录，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/draft/crossdock/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 14. `DraftDirectCreate`

**中文说明：** 创建直送供货申请草稿，根据提交的参数创建新的业务记录，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/draft/direct/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 15. `DraftMultiClusterCreate`

**中文说明：** 创建多集群供货申请草稿，根据提交的参数创建新的业务记录，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/draft/multi-cluster/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 16. `SupplyDraftAPI_DraftSupplyCreate`

**中文说明：** 用于根据草稿创建供货申请，具体用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/draft/supply/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 17. `SupplyDraftAPI_DraftSupplyCreateStatus`

**中文说明：** 获取供货申请创建状态信息，查看当前处理状态、校验结果或执行进度，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/draft/supply/create/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 18. `SupplyDraftAPI_DraftTimeslotInfo`

**中文说明：** 获取可用供货时间段，返回指定对象的详细信息，便于后续判断或处理，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/draft/timeslot/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 19. `SupplyOrderAPI_SupplyOrderCancel`

**中文说明：** 取消供货申请，对指定对象执行取消、删除、拒绝或归档处理，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/cancel`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 20. `SupplyOrderAPI_SupplyOrderCancelStatus`

**中文说明：** 获取供货申请取消状态，查看当前处理状态、校验结果或执行进度，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/cancel/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 21. `SupplyOrderAPI_SupplyOrderContentUpdate`

**中文说明：** 编辑供货商品组成，根据提交的参数更新已有配置、内容或业务状态，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/content/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 22. `SupplyOrderAPI_SupplyOrderContentUpdateStatus`

**中文说明：** 获取供货商品组成编辑状态，查看当前处理状态、校验结果或执行进度，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/content/update/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 23. `SupplyOrderContentUpdateValidation`

**中文说明：** 校验新的供货商品组成，根据提交的参数更新已有配置、内容或业务状态，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/supply-order/content/update/validation`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 24. `SupplyDraftAPI_DraftGetWarehouseFboList`

**中文说明：** 用于搜索供货交货地点，具体用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbo/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 25. `WarehouseFboSellerList`

**中文说明：** 获取卖家仓库列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/fbo/seller/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 26. `CargoesCreateInfoV2`

**中文说明：** 获取设置货运单元的处理信息，用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/cargoes/create/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 27. `DraftCreateInfo`

**中文说明：** 获取供货申请草稿信息，返回指定对象的详细信息，便于后续判断或处理，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/draft/create/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 28. `DraftSupplyCreate`

**中文说明：** 用于根据草稿创建供货申请，具体用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/draft/supply/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 29. `DraftSupplyCreateStatus`

**中文说明：** 获取供货申请创建信息，查看当前处理状态、校验结果或执行进度，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/draft/supply/create/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 30. `DraftTimeslotInfo`

**中文说明：** 获取可用供货时间段列表，返回指定对象的详细信息，便于后续判断或处理，并用于创建 FBO 供货草稿、选择仓库并管理正式供货申请。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/draft/timeslot/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### rFBS Express 仓库创建与管理

方法数量：**5**

#### 1. `WarehouseERFBSAggregatorCreate`

**中文说明：** 创建采用“Ozon 合作伙伴”配送方式的仓库，用于创建和维护 rFBS Express 仓库及配送方式。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/erfbs/aggregator/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `WarehouseERFBSAggregatorDeliveryMethodUpdate`

**中文说明：** 更新“Ozon 合作伙伴”配送方式，用于创建和维护 rFBS Express 仓库及配送方式。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/erfbs/aggregator/delivery-method/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `WarehouseERFBSNonIntegratedCreate`

**中文说明：** 创建采用“卖家或第三方服务”配送方式的仓库，用于创建和维护 rFBS Express 仓库及配送方式。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/erfbs/non-integrated/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `WarehouseERFBSNonIntegratedDeliveryMethodUpdate`

**中文说明：** 更新“卖家或第三方服务”配送方式，用于创建和维护 rFBS Express 仓库及配送方式。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/erfbs/non-integrated/delivery-method/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `WarehouseERFBSUpdate`

**中文说明：** 更新仓库，根据提交的参数更新已有配置、内容或业务状态，并用于创建和维护 rFBS Express 仓库及配送方式。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/warehouse/erfbs/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 定价策略

方法数量：**12**

#### 1. `pricing_competitors`

**中文说明：** 获取竞争对手列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建自动定价策略、绑定商品并根据竞争价格调整售价。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/competitors/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `pricing_create`

**中文说明：** 创建定价策略，根据提交的参数创建新的业务记录，并用于创建自动定价策略、绑定商品并根据竞争价格调整售价。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/create`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `pricing_delete`

**中文说明：** 删除定价策略，对指定对象执行取消、删除、拒绝或归档处理，并用于创建自动定价策略、绑定商品并根据竞争价格调整售价；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 4. `pricing_info`

**中文说明：** 获取定价策略信息，返回指定对象的详细信息，便于后续判断或处理，并用于创建自动定价策略、绑定商品并根据竞争价格调整售价。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `pricing_list`

**中文说明：** 获取定价策略列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建自动定价策略、绑定商品并根据竞争价格调整售价。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 6. `pricing_items-info`

**中文说明：** 获取竞争对手商品价格，返回指定对象的详细信息，便于后续判断或处理，并用于创建自动定价策略、绑定商品并根据竞争价格调整售价。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/product/info`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 7. `pricing_items-add`

**中文说明：** 将商品加入定价策略，用于创建自动定价策略、绑定商品并根据竞争价格调整售价。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/products/add`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 8. `pricing_items-delete`

**中文说明：** 将商品移出定价策略，对指定对象执行取消、删除、拒绝或归档处理，并用于创建自动定价策略、绑定商品并根据竞争价格调整售价；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/products/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 9. `pricing_items-list`

**中文说明：** 获取定价策略中的商品列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于创建自动定价策略、绑定商品并根据竞争价格调整售价。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/products/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `pricing_status`

**中文说明：** 修改定价策略状态，查看当前处理状态、校验结果或执行进度，并用于创建自动定价策略、绑定商品并根据竞争价格调整售价。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 11. `pricing_ids`

**中文说明：** 获取定价策略标识符列表，用于创建自动定价策略、绑定商品并根据竞争价格调整售价。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/strategy-ids-by-product-ids`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 12. `pricing_update`

**中文说明：** 更新定价策略，根据提交的参数更新已有配置、内容或业务状态，并用于创建自动定价策略、绑定商品并根据竞争价格调整售价。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/pricing-strategy/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### FBS/rFBS 标识码与订单组装管理

方法数量：**7**

#### 1. `PostingAPI_FbsPostingProductExemplarUpdate`

**中文说明：** 更新商品实例数据，根据提交的参数更新已有配置、内容或业务状态，并用于校验商品标识码并完成 FBS/rFBS 包裹组装与发货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/fbs/posting/product/exemplar/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `PostingAPI_ShipFbsPostingV4`

**中文说明：** 组装订单（版本 4），用于校验商品标识码并完成 FBS/rFBS 包裹组装与发货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v4/posting/fbs/ship`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `PostingAPI_ShipFbsPostingPackage`

**中文说明：** 用于部分组装包裹（版本 4），具体用于校验商品标识码并完成 FBS/rFBS 包裹组装与发货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v4/posting/fbs/ship/package`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `PostingAPI_FbsPostingProductExemplarStatusV5`

**中文说明：** 获取商品实例添加状态，查看当前处理状态、校验结果或执行进度，并用于校验商品标识码并完成 FBS/rFBS 包裹组装与发货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v5/fbs/posting/product/exemplar/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 5. `PostingAPI_FbsPostingProductExemplarValidateV5`

**中文说明：** 校验商品标识码，用于校验商品标识码并完成 FBS/rFBS 包裹组装与发货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v5/fbs/posting/product/exemplar/validate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `PostingAPI_FbsPostingProductExemplarCreateOrGetV6`

**中文说明：** 获取已创建商品实例的数据，根据提交的参数创建新的业务记录，并用于校验商品标识码并完成 FBS/rFBS 包裹组装与发货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v6/fbs/posting/product/exemplar/create-or-get`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `PostingAPI_FbsPostingProductExemplarSetV6`

**中文说明：** 校验并保存商品实例数据，根据提交的参数更新已有配置、内容或业务状态，并用于校验商品标识码并完成 FBS/rFBS 包裹组装与发货。

- **HTTP 方法：** `POST`
- **接口路径：** `/v6/fbs/posting/product/exemplar/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 财务报告

方法数量：**10**

#### 1. `ReportAPI_GetCompensationReport`

**中文说明：** 获取补偿报告，用于查询交易、结算、补偿和回款数据，用于对账与利润核算。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/finance/compensation`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `ReportAPI_GetDecompensationReport`

**中文说明：** 获取冲销补偿报告，用于查询交易、结算、补偿和回款数据，用于对账与利润核算。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/finance/decompensation`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `ReportAPI_CreateDocumentB2BSalesReport`

**中文说明：** 用于法人客户销售登记表，具体用于查询交易、结算、补偿和回款数据，用于对账与利润核算。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/finance/document-b2b-sales`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `ReportAPI_CreateDocumentB2BSalesJSONReport`

**中文说明：** 用于JSON 格式法人客户销售登记表，具体用于查询交易、结算、补偿和回款数据，用于对账与利润核算。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/finance/document-b2b-sales/json`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `ReportAPI_CreateMutualSettlementReport`

**中文说明：** 获取往来结算报告，用于查询交易、结算、补偿和回款数据，用于对账与利润核算。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/finance/mutual-settlement`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `GetFinanceProductsBuyout`

**中文说明：** 获取已买断商品报告，用于查询交易、结算、补偿和回款数据，用于对账与利润核算。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/finance/products/buyout`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 7. `FinanceAPI_GetRealizationReportV1`

**中文说明：** 按订单统计的商品销售结算报告，用于查询交易、结算、补偿和回款数据，用于对账与利润核算。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/finance/realization/posting`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `FinanceAPI_GetRealizationReportV2`

**中文说明：** 用于商品销售结算报告（版本 2），具体用于查询交易、结算、补偿和回款数据，用于对账与利润核算。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/finance/realization`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `FinanceAPI_FinanceTransactionListV3`

**中文说明：** 获取交易列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查询交易、结算、补偿和回款数据，用于对账与利润核算。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/finance/transaction/list`
- **安全级别：** 只读
- **订阅要求：** PREMIUM

---

#### 10. `FinanceAPI_FinanceTransactionTotalV3`

**中文说明：** 获取交易金额汇总，用于查询交易、结算、补偿和回款数据，用于对账与利润核算。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/finance/transaction/totals`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 商品价格与库存

方法数量：**11**

#### 1. `ProductAPI_ActionTimerStatus`

**中文说明：** 获取已设置计时器的状态，查看当前处理状态、校验结果或执行进度，并用于查询或更新商品价格、最低价、佣金和仓库库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/action/timer/status`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `ProductAPI_ActionTimerUpdate`

**中文说明：** 更新最低价有效期计时器，根据提交的参数更新已有配置、内容或业务状态，并用于查询或更新商品价格、最低价、佣金和仓库库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/action/timer/update`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `ProductAPI_ImportProductsPrices`

**中文说明：** 更新商品价格，将文件或业务数据提交到 Ozon 进行导入和处理，并用于查询或更新商品价格、最低价、佣金和仓库库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/import/prices`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `ProductAPI_GetProductInfoDiscounted`

**中文说明：** 按折价商品 SKU 获取折价信息及原商品信息，用于查询或更新商品价格、最低价、佣金和仓库库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/info/discounted`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `ProductAPI_ProductStocksByWarehouseFbs`

**中文说明：** 用于卖家仓库库存信息（FBS 和 rFBS），具体用于查询或更新商品价格、最低价、佣金和仓库库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/info/stocks-by-warehouse/fbs`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `ProductInfoWarehouseStocks`

**中文说明：** 获取 FBS 和 rFBS 仓库库存信息，用于查询或更新商品价格、最低价、佣金和仓库库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/info/warehouse/stocks`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 7. `ProductAPI_ProductUpdateDiscount`

**中文说明：** 为折价商品设置折扣，根据提交的参数更新已有配置、内容或业务状态，并用于查询或更新商品价格、最低价、佣金和仓库库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/product/update/discount`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 8. `ProductAPI_GetProductInfoStocksByWarehouseFbsV2`

**中文说明：** 获取卖家仓库库存信息，返回指定对象的详细信息，便于后续判断或处理，并用于查询或更新商品价格、最低价、佣金和仓库库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/product/info/stocks-by-warehouse/fbs`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `ProductAPI_ProductsStocksV2`

**中文说明：** 更新仓库商品数量，用于查询或更新商品价格、最低价、佣金和仓库库存。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/products/stocks`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 10. `ProductAPI_GetProductInfoStocks`

**中文说明：** 获取商品在 Ozon 各履约模式下的现有数量和预留数量，用于库存同步与可售库存判断。

- **HTTP 方法：** `POST`
- **接口路径：** `/v4/product/info/stocks`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 11. `ProductAPI_GetProductInfoPrices`

**中文说明：** 批量获取商品当前售价、营销价、最低价、价格指数和佣金等信息，用于定价与利润分析。

- **HTTP 方法：** `POST`
- **接口路径：** `/v5/product/info/prices`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 买家聊天

方法数量：**4**

#### 1. `ChatAPI_ChatSendFile`

**中文说明：** 发送文件，用于查看买家会话并发送文字或文件消息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/chat/send/file`
- **安全级别：** 写入
- **订阅要求：** PREMIUM_PLUS

---

#### 2. `ChatAPI_ChatListV2`

**中文说明：** 获取聊天列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查看买家会话并发送文字或文件消息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v2/chat/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `ChatAPI_ChatHistoryV3`

**中文说明：** 获取聊天记录，用于查看买家会话并发送文字或文件消息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/chat/history`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `ChatAPI_ChatListV3`

**中文说明：** 获取聊天列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于查看买家会话并发送文字或文件消息。

- **HTTP 方法：** `POST`
- **接口路径：** `/v3/chat/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 小票

方法数量：**3**

#### 1. `GetReceipt`

**中文说明：** 获取 PDF 格式小票，返回指定对象的详细信息，便于后续判断或处理，并用于上传或查询卖家向买家提供的电子小票。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/receipts/get`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `ReceiptsSellerList`

**中文说明：** 获取卖家小票列表，返回符合筛选条件的记录列表，便于后续查询或批量处理，并用于上传或查询卖家向买家提供的电子小票。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/receipts/seller/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `UploadReceipt`

**中文说明：** 上传小票，将文件或业务数据提交到 Ozon 进行导入和处理，并用于上传或查询卖家向买家提供的电子小票。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/receipts/upload`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 商品条码

方法数量：**2**

#### 1. `add-barcode`

**中文说明：** 将条码绑定到商品，用于为商品生成条码或将已有条码绑定到商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/barcode/add`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `generate-barcode`

**中文说明：** 为商品生成条码，用于为商品生成条码或将已有条码绑定到商品。

- **HTTP 方法：** `POST`
- **接口路径：** `/v1/barcode/generate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

## 广告绩效 API

方法数量：**46**

### 外部流量分析

方法数量：**4**

#### 1. `GetVendorTag`

**中文说明：** 用于外部广告活动的组织标记，具体用于统计外部广告或站外流量带来的访问、订单和转化效果。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/organisation/vendor_tag`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `VendorStatisticsSubmitRequest`

**中文说明：** 获取外部流量分析报告，生成、查询或下载相应的统计与经营报告，并用于统计外部广告或站外流量带来的访问、订单和转化效果。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/vendors/statistics`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `VendorStatisticsListReports`

**中文说明：** 获取已申请的外部流量分析报告列表，用于统计外部广告或站外流量带来的访问、订单和转化效果。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/vendors/statistics/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `VendorStatisticsCheck`

**中文说明：** 按 UUID 获取报告信息，用于统计外部广告或站外流量带来的访问、订单和转化效果。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/vendors/statistics/{UUID}`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 广告活动与推广对象

方法数量：**5**

#### 1. `ListCampaigns`

**中文说明：** 获取广告账户中的广告活动列表及其基础状态，用于筛选和管理当前投放中的广告活动。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/campaign`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 2. `ListCampaignObjects`

**中文说明：** 获取广告活动中的推广对象列表，用于查询广告活动、推广商品及广告工具的出价限制。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/campaign/{campaignId}/objects`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 3. `GetLimitsList`

**中文说明：** 用于推广工具出价限制，具体用于查询广告活动、推广商品及广告工具的出价限制。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/limits/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 4. `ExternalCampaign_BidBySKU`

**中文说明：** 按 SKU 获取商品最低出价，用于查询广告活动、推广商品及广告工具的出价限制。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/min/sku`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `ExternalCampaign_ListProductsWithBonuses2`

**中文说明：** 获取含奖励金的商品列表，用于查询广告活动、推广商品及广告工具的出价限制。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/products_with_bonuses`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 按订单付费推广

方法数量：**11**

#### 1. `ActivateAllSkuPromoCampaign`

**中文说明：** 启用按订单付费推广——全部商品，用于管理按订单付费推广中的商品、出价和启停状态。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/campaign/all_sku_promo/activate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `DeactivateAllSkuPromoCampaign`

**中文说明：** 停用按订单付费推广——全部商品，用于管理按订单付费推广中的商品、出价和启停状态。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/campaign/all_sku_promo/deactivate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `ExternalCampaign_BatchDisableCarrots4`

**中文说明：** 停用“胡萝卜城”促销活动中的商品推广，用于管理按订单付费推广中的商品、出价和启停状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/campaign/search_promo/carrots/disable`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `ExternalCampaign_BatchEnableCarrots4`

**中文说明：** 启用“胡萝卜城”促销活动中的商品推广，用于管理按订单付费推广中的商品、出价和启停状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/campaign/search_promo/carrots/enable`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `ExternalCampaign_DeleteSearchPromoBidsV2`

**中文说明：** 从按订单付费推广中移除商品，用于管理按订单付费推广中的商品、出价和启停状态；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/campaign/search_promo/v2/bids/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 6. `ExternalCampaign_SetSearchPromoBidsV2`

**中文说明：** 设置商品出价，根据提交的参数更新已有配置、内容或业务状态，并用于管理按订单付费推广中的商品、出价和启停状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/campaign/search_promo/v2/bids/set`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `ExternalCampaign_ListSearchPromoProductsV2`

**中文说明：** 按订单付费推广商品列表，用于管理按订单付费推广中的商品、出价和启停状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/campaign/search_promo/v2/products`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `ExternalCampaign_GetProductsRecommendedBids`

**中文说明：** 用于商品推荐出价，具体用于管理按订单付费推广中的商品、出价和启停状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/search_promo/bids/recommendation`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 9. `ExternalCampaign_GetCPOMinBids`

**中文说明：** 获取商品固定出价，返回指定对象的详细信息，便于后续判断或处理，并用于管理按订单付费推广中的商品、出价和启停状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/search_promo/get_cpo_min_bids`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 10. `ExternalCampaign_BatchDisableProducts`

**中文说明：** 停用商品的按订单付费推广，用于管理按订单付费推广中的商品、出价和启停状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/search_promo/product/disable`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 11. `ExternalCampaign_BatchEnableProducts`

**中文说明：** 启用商品的按订单付费推广，用于管理按订单付费推广中的商品、出价和启停状态。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/search_promo/product/enable`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 按点击付费推广

方法数量：**5**

#### 1. `CreateProductCampaignCPCV2`

**中文说明：** 创建按点击付费广告活动，用于创建和管理 CPC 广告活动、预算、状态及投放参数。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/campaign/cpc/v2/product`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `PatchProductCampaign`

**中文说明：** 获取广告活动参数，用于创建和管理 CPC 广告活动、预算、状态及投放参数。

- **HTTP 方法：** `PATCH`
- **接口路径：** `/api/client/campaign/{campaignId}`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `ActivateCampaign`

**中文说明：** 启用广告活动，用于创建和管理 CPC 广告活动、预算、状态及投放参数。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/campaign/{campaignId}/activate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `DeactivateCampaign`

**中文说明：** 停用广告活动，用于创建和管理 CPC 广告活动、预算、状态及投放参数。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/campaign/{campaignId}/deactivate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `CalculateDynamicBudget`

**中文说明：** 计算广告活动最低预算，用于创建和管理 CPC 广告活动、预算、状态及投放参数。

- **HTTP 方法：** `POST`
- **接口路径：** `/external/api/dynamic_budget`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

### 统计数据

方法数量：**16**

#### 1. `SearchPromoOrdersReportSubmitRequest`

**中文说明：** 获取按订单付费推广订单报告——指定商品，用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/statistic/orders/generate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `SearchPromoProductsReportSubmitRequest`

**中文说明：** 获取按订单付费推广商品报告——指定商品，用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/statistic/products/generate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `SubmitRequest`

**中文说明：** 提交广告活动统计报告任务，用于按指定时间和筛选条件统计曝光、点击、花费及其他投放指标。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/statistics`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `GenerateAllSkuPromoOrdersReport`

**中文说明：** 获取按订单付费推广订单报告——全部商品，用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/statistics/all_sku_promo/orders/generate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 5. `GenerateAllSkuPromoProductsReport`

**中文说明：** 获取按订单付费推广商品报告——全部商品，用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/statistics/all_sku_promo/products/generate`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 6. `AttributionSubmitRequest`

**中文说明：** 获取订单归因报告，生成、查询或下载相应的统计与经营报告，并用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/statistics/attribution`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 7. `MediaCampaignList`

**中文说明：** 获取展示类广告活动统计，生成、查询或下载相应的统计与经营报告，并用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/statistics/campaign/media`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 8. `ProductCampaignList`

**中文说明：** 按点击付费广告活动统计，生成、查询或下载相应的统计与经营报告，并用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/statistics/campaign/product`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 9. `GetCampaignDailyStats`

**中文说明：** 获取广告活动每日统计，生成、查询或下载相应的统计与经营报告，并用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/statistics/daily`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 10. `GetCampaignExpense`

**中文说明：** 获取广告活动支出统计，生成、查询或下载相应的统计与经营报告，并用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/statistics/expense`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 11. `ListReportsExternal`

**中文说明：** 获取通过 API 生成的报告列表，用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/statistics/externallist`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 12. `ListReports`

**中文说明：** 获取通过后台界面生成的报告列表，用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/statistics/list`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 13. `ExternalStatistics_StatisticsPhrasesSubmitRequest2`

**中文说明：** 获取搜索词报告，生成、查询或下载相应的统计与经营报告，并用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/statistics/phrases`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 14. `DownloadStatistics`

**中文说明：** 下载已经生成完成的广告统计报告文件，用于进一步分析投放表现或导入本地系统。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/statistics/report`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

#### 15. `VideoCampaignsSubmitRequest`

**中文说明：** 获取视频横幅展示统计，生成、查询或下载相应的统计与经营报告，并用于生成并下载广告曝光、点击、花费、订单和归因等统计报告。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/statistics/video`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 16. `StatisticsCheck`

**中文说明：** 根据报告 UUID 查询广告统计报告的生成状态，用于判断报告是否可以下载。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/statistics/{UUID}`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---

### 按点击付费与特别展示中的商品

方法数量：**5**

#### 1. `AddProducts`

**中文说明：** 将商品加入广告活动，用于管理 CPC 或特别展示广告中的商品和商品出价。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/campaign/{campaignId}/products`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 2. `UpdateProducts`

**中文说明：** 更新商品出价，用于管理 CPC 或特别展示广告中的商品和商品出价。

- **HTTP 方法：** `PUT`
- **接口路径：** `/api/client/campaign/{campaignId}/products`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 3. `GetProductsCompetitiveBids`

**中文说明：** 用于商品竞争出价，具体用于管理 CPC 或特别展示广告中的商品和商品出价。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/campaign/{campaignId}/products/bids/competitive`
- **安全级别：** 写入
- **订阅要求：** 无特殊订阅要求

---

#### 4. `DeleteProducts`

**中文说明：** 将商品移出广告活动，对指定对象执行取消、删除、拒绝或归档处理，并用于管理 CPC 或特别展示广告中的商品和商品出价；调用前应确认目标对象和业务条件。

- **HTTP 方法：** `POST`
- **接口路径：** `/api/client/campaign/{campaignId}/products/delete`
- **安全级别：** 破坏性
- **订阅要求：** 无特殊订阅要求

---

#### 5. `GetProductsV2`

**中文说明：** 获取广告活动商品列表，用于管理 CPC 或特别展示广告中的商品和商品出价。

- **HTTP 方法：** `GET`
- **接口路径：** `/api/client/campaign/{campaignId}/v2/products`
- **安全级别：** 只读
- **订阅要求：** 无特殊订阅要求

---
