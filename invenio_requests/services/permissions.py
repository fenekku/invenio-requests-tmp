"""Request permissions."""

from itertools import chain

from invenio_access.permissions import any_user
from invenio_records_permissions import RecordPermissionPolicy
from invenio_records_permissions.generators import Generator
from invenio_records_permissions.generators import AnyUser, SystemProcess

from .services import RequestEventType


class Requesters(Generator):
    """Allows request makers."""

    def needs(self, request=None, **kwargs):
        """Enabling Needs.

        record is a request here
        """
        # TODO when request is more fleshed out
        return [any_user]
        # return [
        #     UserNeed(owner.owner_id) for owner in record.access.owners
        # ]
        # even above could be optimized without caching by using raw ids


    def query_filter(self, identity=None, **kwargs):
        """Filters for current identity as owner."""
        # TODO when request is more fleshed out
        return []


class Reviewers(Generator):
    """Allows request reviewers."""

    def needs(self, request=None, **kwargs):
        """Enabling Needs.

        record is a request here
        """
        # TODO when request is more fleshed out
        return [any_user]
        # return [
        #     UserNeed(owner.owner_id) for owner in record.access.owners
        # ]
        # even above could be optimized without caching by using raw ids


    def query_filter(self, identity=None, **kwargs):
        """Filters for current identity as owner."""
        # TODO when request is more fleshed out
        return []


class Commenter(Generator):
    """Allows request event commenter."""

    def needs(self, request=None, **kwargs):
        """Enabling Needs.

        record is a request here
        """
        # TODO when request is more fleshed out
        return [any_user]
        # return [UserNeed(record.owner)]


# Requests
# TODO
# can_search = [SystemProcess(), AnyUser()]
# can_read = [SystemProcess(), AnyUser()]
# can_create = [SystemProcess()]
# can_update = [SystemProcess()]
# can_delete = [SystemProcess()]
# can_manage = [SystemProcess()]

# class IfComment(Generator):
#     """."""

#     def __init__(self, *generators):
#         """Constructor."""
#         self._generators = generators

#     def needs(self, request=None, **kwargs):
#         """Set of Needs granting permission."""
#         if event["type"] == RequestEventType.COMMENT:
#             needs = [
#                 g.needs(request=request, **kwargs) for g in self._generators
#             ]
#             return set(chain.from_iterable(needs))
#         return frozenset()

#     def excludes(self, request=None, **kwargs):
#         """Set of Needs denying permission."""
#         if request["type"] == RequestEventType.COMMENT:
#             excludes = [
#                 g.excludes(request=request, **kwargs) for g in self._generators
#             ]
#             return set(chain.from_iterable(excludes))
#         return frozenset()


class RequestEventsPermissionPolicy(RecordPermissionPolicy):
    """Events Permission policy."""
    # Comment is a special case
    can_create_event_comment = [Requesters(), Reviewers(), SystemProcess()]


    can_update_event_comment = [Commenter(), SystemProcess()]  # Comment maker
    # Requester + Reviewer(for spam)
    can_delete_event_comment = [Commenter(), Reviewers(), SystemProcess()]

    # those are never used since the more general ones below cover them
    # can_read_event_comment = []  # Requester + Reviewer
    # can_search_event_comment = []  # Requester + Reviewer

    # Other events are all the same
    # can_create_event_other = [SystemProcess()]  # system
    can_read_event_other = [SystemProcess()]  # Requester + Reviewer
    can_update_event_other = [SystemProcess()]  # system
    can_delete_event_other = [SystemProcess()]  # system
    can_search_event_other = [SystemProcess()]  # Requester + Reviewer
