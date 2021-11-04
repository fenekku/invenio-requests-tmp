# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Northwestern University.
# Copyright (C) 2021 TU Wien.
#
# Invenio-Requests is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.


from invenio_records_resources.services.records.schema import BaseRecordSchema
from marshmallow import fields


class RequestEventSchema(BaseRecordSchema):
    """Schema."""
    type = fields.Str(required=True)
