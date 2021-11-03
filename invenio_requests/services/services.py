# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 Northwestern University.
# Copyright (C) 2021 TU Wien.
#
# Invenio-Requests is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

from invenio_db import db
from invenio_records_resources.services import RecordService

from ..records.api import Request


class RequestsService(RecordService):
    """RequestsService."""
    pass


# TODO: Implement me
class CommentResultItem:
    """Comment Result Item."""

    def __init__(self):
        """Constructor."""
        self.id = 1


class RequestEventType:
    """dummy enum like for now."""

    COMMENT = "C"


class EventResultItem:
    """Event Result Item."""

    def __init__(self):
        """Constructor."""
        pass

class RequestEventsService(RecordService):
    """Request Events service."""

    # type: comment action: create -> create (users + system)
    # type: comment action: edit -> edit (users + system)
    # ...

    # type: edit action: create -> create_edit_event  (system)
    # type: edit action: edit -> edit_edit_event  (system)
    # ...

    # type: accept -> create_accept_event (system)

    # pros: explicit, cons: verbose

    # OR

    # type: comment -> create_comment
    # type: edit/accept/decline -> create_comment



    def create(self, identity, request_id, data):
        """Create a request event.

        :param request_id: Identifier of the request.
        :param identity: Identity of user creating the event.
        :param dict data: Input data according to the data schema.
        """
        request = self._get_request(request_id)
        permission = self._get_permission("create", data["type"])
        self.require_permission(identity, permission, request=request)

        # Validate data and create record with pid
        # data["request"] = request
        data, errors = self.schema.load(
            data,
            context={"identity": identity},
        )

        # It's the components that save the actual data in the record.
        record = self.record_cls.create({})

        # Run components
        self.run_components(
            "create_event",
            identity=identity,
            record=record,
            request=request,
            data=data
        )

        # Persist record (DB and index)
        record.commit()
        db.session.commit()
        if self.indexer:
            self.indexer.index(record)

        return self.result_item(
            self,
            identity,
            record,
            links_tpl=self.links_item_tpl,
        )

    def _get_permission(self, action, event_type):
        """Get associated permission.

        Needed to distinguish between comment creation and other events.
        """
        if event_type == RequestEventType.COMMENT:
            if action == "create":
                return "create_event_comment"
        else:
            if action == "create":
                return "create_event_other"

    def _get_request(self, request_id):
        """Get associated request."""
        return Request.pid.resolve(request_id, registered_only=False)
