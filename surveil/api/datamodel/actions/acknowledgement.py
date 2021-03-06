# Copyright 2014 - Savoir-Faire Linux inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import wsme
import wsme.types as wtypes

from surveil.api.datamodel import types


class Acknowledgement(types.Base):
    host_name = wsme.wsattr(wtypes.text, mandatory=True)
    """The name of the host"""

    service_description = wsme.wsattr(wtypes.text, mandatory=False)

    time_stamp = wsme.wsattr(wtypes.text, mandatory=False)

    sticky = wsme.wsattr(int, mandatory=False)

    notify = wsme.wsattr(int, mandatory=False)

    persistent = wsme.wsattr(int, mandatory=False)

    author = wsme.wsattr(wtypes.text, mandatory=False)

    comment = wsme.wsattr(wtypes.text, mandatory=False)

    @classmethod
    def sample(cls):
        return cls(
            host_name="localhost",
            service_description="ws-arbiter",
            time_stamp="",
            sticky=1,
            notify=0,
            persistent=1,
            author="aviau",
            comment="Working on it.",
        )
