# -*- coding: utf-8 -*-
import entity

# entity.application('php')
entity.application('py')
# entity.application('ts')

# 言語依存
# 1.ドメイン層
# 2.インフラストラクチャー層
# 3.アプリケーション層
# 4.アプリケーション層テストコード(Unit)

# フレームワーク依存
# 1.プレゼンテーション層
# 2.プレゼンテーション層テストコード(E2E)

# print('sugumi起動。本日目標はアプリケーション層の起動のみ')
import usecase
usecase.presentation('flask', 'py')
