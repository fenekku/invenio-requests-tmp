# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 TU Wien.
#
# Invenio-Requests is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""Base classes for requests in Invenio."""

import uuid

from invenio_db import db
from invenio_records.models import RecordMetadataBase
from sqlalchemy_utils import UUIDType


class RequestMetadata(db.Model, RecordMetadataBase):
    """Base class for requests of any kind in Invenio."""

    __tablename__ = "requests_metadata"

    id = db.Column(UUIDType, primary_key=True, default=uuid.uuid4)

    # TODO later
    # labels: maybe per-community CVs
    # prerequisites for each action: like checks in GitHub actions
    # assignees: enables notifications? no impact on permissions


class RequestEventModel(db.Model, RecordMetadataBase):
    """Request Events model."""

    __tablename__ = "request_events"

    type = db.Column(db.String(1), nullable=False)
    request_id = db.Column(
        UUIDType,
        db.ForeignKey(RequestMetadata.id, ondelete="CASCADE")
    )
    request = db.relationship(RequestMetadata)
