# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Northwestern University.
# Copyright (C) 2021 TU Wien.
#
# Invenio-Requests is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


from invenio_records_resources.services import RecordServiceConfig
from invenio_records_resources.services.records.components import \
    DataComponent

from ..records.api import RequestEvent
from .components import RequestComponent
from .permissions import RequestEventsPermissionPolicy
from .schemas import RequestEventSchema


class RequestsServiceConfig(RecordServiceConfig):
    pass


class RequestEventsServiceConfig(RecordServiceConfig):
    """Config."""
    permission_policy_cls = RequestEventsPermissionPolicy
    record_cls = RequestEvent
    schema = RequestEventSchema

    components = [
        RequestComponent,
        DataComponent,
    ]
