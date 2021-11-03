# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Northwestern University.
# Copyright (C) 2021 TU Wien.
#
# Invenio-Requests is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"Components."

from invenio_records_resources.services.records.components import \
    ServiceComponent


class RequestComponent(ServiceComponent):
    """Component that injects the related request into the event."""

    def create_event(
            self, identity=None, record=None, request=None, data=None):
        """Inject request in event (record)."""
        import pdb; pdb.set_trace()  # STOPPED HERE
        record.request = request

    def update(self, identity, data=None, record=None, **kwargs):
        """Inject vocabulary type to the record."""
        self._set_type(data, record)
