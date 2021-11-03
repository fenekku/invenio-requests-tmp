import pytest

from invenio_requests.services.services import RequestEventType


@pytest.fixture()
def example_record(app, db, input_data):
    """Example data layer record."""
    record = Record.create({}, **input_data)
    db.session.commit()
    return record


@pytest.fixture()
def events_service_data():
    """Input data for the Request Events Service."""
    return {
        "type": RequestEventType.COMMENT
    }
