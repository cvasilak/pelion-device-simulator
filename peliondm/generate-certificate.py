# ---------------------------------------------------------------------------
# Pelion Device Management SDK
# (C) COPYRIGHT 2017 Arm Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------------------------------------------------
"""generate a developer certificate and output a mbed_cloud_dev_credentials.c file."""

import os
import logging

from mbed_cloud import AccountManagementAPI, CertificatesAPI

LOG = logging.getLogger(' generate-certificate ')

def _main():
   config = {}

   try:
       config["api_key"] = os.environ['CLOUD_SDK_API_KEY']
   except KeyError as e:
       LOG.error(
           'Missing CLOUD_SDK_API_KEY enviromental key !'
       )
       exit(1)

   accounts = AccountManagementAPI(config)
   certs = CertificatesAPI(config)

   api_key_value = accounts.config.get("api_key")
   api_key = next(accounts.list_api_keys(
       filter={
           "key": api_key_value
       }
   ))

   certificates_owned = list(certs.list_certificates())
   dev_cert_info = None
   for certif in certificates_owned:
       if certif.type == "developer" and (certif.owner_id == api_key.owner_id or
                                          certif.owner_id == api_key.id):
           dev_cert_info = certs.get_certificate(certif.id)
           LOG.info("Found developer certificate named '%s'",
                    dev_cert_info.name)
           break
   else:
       LOG.warning(
           "Could not find developer certificate for this account."
           " Generating a new developer certificate."
       )
       dev_cert_info = certs.add_developer_certificate(
           "mbed-cli-auto {}".format(api_key.name),
           description="cetificate auto-generated by pelion-device-simulator"
       )

   LOG.info("Writing developer certificate %s into c file "
       "'mbed_cloud_dev_credentials.c'", dev_cert_info.name)
   with open("mbed_cloud_dev_credentials.c", "w") as fout:
      fout.write(dev_cert_info.header_file)

if __name__ == "__main__":
    _main()
