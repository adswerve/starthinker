###########################################################################
#
#  Copyright 2021 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################
#
#  This code generated (see scripts folder for possible source):
#    - Command: "python starthinker_ui/manage.py example"
#
###########################################################################

import argparse
import textwrap

from starthinker.util.configuration import Configuration
from starthinker.task.smartsheet.run import smartsheet


def recipe_smartsheet_to_bigquery(config, auth_read, auth_write, token, sheet, dataset, table, schema, link):
  """Move sheet data into a BigQuery table.

     Args:
       auth_read (authentication) - Credentials used for reading data.
       auth_write (authentication) - Credentials used for writing data.
       token (string) - Retrieve from SmartSheet account settings.
       sheet (string) - Retrieve from sheet properties.
       dataset (string) - Existing BigQuery dataset.
       table (string) - Table to create from this report.
       schema (json) - Schema provided in JSON list format or leave empty to auto detect.
       link (boolean) - Add a link to each row as the first column.
  """

  smartsheet(config, {
    'auth':auth_read,
    'token':token,
    'sheet':sheet,
    'link':link,
    'out':{
      'bigquery':{
        'auth':auth_write,
        'dataset':dataset,
        'table':table,
        'schema':schema
      }
    }
  })



if __name__ == "__main__":
  parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent("""
      Move sheet data into a BigQuery table.

        1. Specify <a href='https://smartsheet-platform.github.io/api-docs/' target='_blank'>SmartSheet</a> token.
        2. Locate the ID of a sheet by viewing its properties.
        3. Provide a BigQuery dataset ( must exist ) and table to write the data into.
        4. StarThinker will automatically map the correct schema.
  """))

  parser.add_argument("-project", help="Cloud ID of Google Cloud Project.", default=None)
  parser.add_argument("-key", help="API Key of Google Cloud Project.", default=None)
  parser.add_argument("-client", help="Path to CLIENT credentials json file.", default=None)
  parser.add_argument("-user", help="Path to USER credentials json file.", default=None)
  parser.add_argument("-service", help="Path to SERVICE credentials json file.", default=None)
  parser.add_argument("-verbose", help="Print all the steps as they happen.", action="store_true")

  parser.add_argument("-auth_read", help="Credentials used for reading data.", default='user')
  parser.add_argument("-auth_write", help="Credentials used for writing data.", default='service')
  parser.add_argument("-token", help="Retrieve from SmartSheet account settings.", default='')
  parser.add_argument("-sheet", help="Retrieve from sheet properties.", default=None)
  parser.add_argument("-dataset", help="Existing BigQuery dataset.", default='')
  parser.add_argument("-table", help="Table to create from this report.", default='')
  parser.add_argument("-schema", help="Schema provided in JSON list format or leave empty to auto detect.", default=None)
  parser.add_argument("-link", help="Add a link to each row as the first column.", default=True)


  args = parser.parse_args()

  config = Configuration(
    project=args.project,
    user=args.user,
    service=args.service,
    client=args.client,
    key=args.key,
    verbose=args.verbose
  )

  recipe_smartsheet_to_bigquery(config, args.auth_read, args.auth_write, args.token, args.sheet, args.dataset, args.table, args.schema, args.link)
