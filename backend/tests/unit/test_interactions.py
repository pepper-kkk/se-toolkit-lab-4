"""Unit tests for interaction filtering logic."""

from app.models.interaction import InteractionLog
from app.routers.interactions import _filter_by_item_id  # noqa: SLF001


def _make_log(id: int, learner_id: int, item_id: int) -> InteractionLog:
    return InteractionLog(id=id, learner_id=learner_id, item_id=item_id, kind="attempt")


def test_filter_returns_all_when_item_id_is_none() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, None)
    assert result == interactions


def test_filter_returns_empty_for_empty_input() -> None:
    result = _filter_by_item_id([], 1)
    assert result == []


def test_filter_returns_interaction_with_matching_ids() -> None:
    interactions = [_make_log(1, 1, 1), _make_log(2, 2, 2)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1


def test_filter_excludes_interaction_with_different_learner_id() -> None:
    interactions = [_make_log(1, 2, 1)]
    result = _filter_by_item_id(interactions, 1)
    assert len(result) == 1
    assert result[0].id == 1


def test_filter_returns_empty_when_no_item_id_matches() -> None:
    interactions = [_make_log(1, 1, 10), _make_log(2, 2, 20)]
    result = _filter_by_item_id(interactions, 999)
    assert result == []


def test_filter_returns_multiple_matches_for_same_item_id() -> None:
    interactions = [_make_log(1, 1, 7), _make_log(2, 2, 7), _make_log(3, 3, 9)]
    result = _filter_by_item_id(interactions, 7)
    assert len(result) == 2
    assert [x.id for x in result] == [1, 2]


# Discarded AI idea (example): test behavior for negative item_id.
# Reason: API/logic doesn't define meaning for negative item_id, so test would be out of scope.
