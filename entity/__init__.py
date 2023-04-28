# -*- coding: utf-8 -*-

import json
import codecs
import util
import os

def mkdir(dir: str):
    if not os.path.isdir(dir):
        os.mkdir(dir)
    return

def test():
    domain_file_name = 'entity/entity.json'
    domain_file = codecs.open(domain_file_name, 'r', 'utf8')
    domain_dict = json.load(domain_file)
    for entity in domain_dict.get('entityList'):
        entity_name = entity['name']

        # ドメイン層の出力ルートディレクトリ作成
        # value_object_root = f'../src/lib'
        # value_object_output_dir = f'{value_object_root}/{entity_name}'
        # if not os.path.isdir(value_object_output_dir):
        #     os.mkdir(value_object_output_dir)
        entity_root = f'../src/lib/server'
        entity_output_dir = f'{entity_root}/{entity_name}'
        mkdir(entity_output_dir)
        # プレゼンテーション層(今はひとまずsvelte、e2eはplaywright)
        mkdir(f'../src/routes/{entity_name}')
        if not os.path.isdir(f'../tests/{entity_name}'):
            os.mkdir(f'../tests/{entity_name}')
        if not os.path.isdir(f'../src/routes/api/{entity_name}'):
            os.mkdir(f'../src/routes/api/{entity_name}')
        util.create_concrete_from_params('presentation/+server.ts.j2', entity, f'../src/routes/api/{entity_name}/+server.ts')
        util.create_concrete_from_params('presentation/+page.server.ts.j2', entity, f'../src/routes/{entity_name}/+page.server.ts')
        util.create_concrete_from_params('presentation/+page.svelte.j2', entity, f'../src/routes/{entity_name}/+page.svelte')
        util.create_concrete_from_params('presentation/test.ts.j2', entity, f'../tests/{entity_name}/{entity_name}.test.ts')

        # ドメイン層の出力ルートディレクトリ作成
        # value_object_root = f'../src/lib'
        # value_object_output_dir = f'{value_object_root}/{entity_name}'
        # if not os.path.isdir(value_object_output_dir):
        #     os.mkdir(value_object_output_dir)
        entity_root = f'../src/lib/server'
        entity_output_dir = f'{entity_root}/{entity_name}'
        if not os.path.isdir(entity_output_dir):
            os.mkdir(entity_output_dir)
        # エンティティ
        util.create_concrete_from_params('entity/entity.ts.j2', entity, f'{entity_output_dir}/{entity_name}.ts')
        util.create_concrete_from_params('entity/entity.test.ts.j2', entity, f'{entity_output_dir}/{entity_name}.test.ts')

        # アプリケーション層の出力ルートディレクトリ作成
        application_root = f'../src/lib/server'
        application_output_dir = f'{application_root}/{entity_name}'
        if not os.path.isdir(application_output_dir):
            os.mkdir(application_output_dir)
        # アプリケーション層とそのテストコード
        util.create_concrete_from_params('entity/applicationService.ts.j2', entity, f'{application_output_dir}/{entity_name}ApplicationService.ts')
        util.create_concrete_from_params('entity/applicationService.test.ts.j2', entity, f'{application_output_dir}/{entity_name}ApplicationService.test.ts')
    return

# エンティティのイコールは識別子が一致していることであり、
# 値オブジェクトのイコールは全てのメンバが一致しているってことかな?

# アプリケーション層より内側CLIから動作できるものを作成する
def application(extension: str):
    #extension = 'php'
    output_root = f'../{extension}'
    mkdir(output_root)
    domain_root = f'{output_root}/Domain'
    mkdir(domain_root)
    value_object_root = f'{domain_root}/ValueObject'
    mkdir(value_object_root)
    #infrastructure_root = f'{output_root}/Infrastructure'
    #mkdir(infrastructure_root)
    application_root = f'{output_root}/Application'
    mkdir(application_root)
    domain_file_name = 'entity/entity.json'
    domain_file = codecs.open(domain_file_name, 'r', 'utf8')
    domain_dict = json.load(domain_file)
    for entity in domain_dict.get('entityList'):
        domain_name = entity['name']

        # ドメイン層
        entity_output_dir = f'{domain_root}/{domain_name}'
        mkdir(entity_output_dir)
        util.create_concrete_from_params(f'entity/{extension}/entity.{extension}.j2', entity, f'{entity_output_dir}/{domain_name}.{extension}')

        # インフラストラクチャー層(使わないかもしれないので今はインフラストラクチャー層は無し)
        # infrastructure_output_dir = f'{infrastructure_root}/{domain_name}'
        # mkdir(infrastructure_output_dir)
        # util.create_concrete_from_params('entity/infrastructure.ts.j2', entity, f'{infrastructure_output_dir}/{domain_name}.php')

        # アプリケーション層
        application_output_dir = f'{application_root}/{domain_name}'
        mkdir(application_output_dir)
        util.create_concrete_from_params(f'entity/{extension}/applicationService.{extension}.j2', entity, f'{application_output_dir}/{domain_name}ApplicationService.{extension}')
    return