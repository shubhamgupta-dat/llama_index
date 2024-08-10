# coding: utf-8

"""
    Manager

    Subscription management and related services.

    The version of the OpenAPI document: 1.0
    Contact: hello@wordlift.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self


class VectorSearchQueryResponseItem(BaseModel):
    """
    An array of objects.
    """  # noqa: E501

    embeddings: Optional[List[Union[StrictFloat, StrictInt]]] = Field(
        default=None, description="The embeddings for the text."
    )
    id: Optional[StrictStr] = None
    metadata: Optional[Dict[str, Dict[str, Any]]] = Field(
        default=None, description="A nodes extra metadata."
    )
    node_id: StrictStr = Field(description="A nodes id.")
    score: Union[StrictFloat, StrictInt] = Field(
        description="The similarity score between the node and the query embeddings."
    )
    text: StrictStr = Field(
        description="The text of a node from which the embeddings were generated."
    )
    __properties: ClassVar[List[str]] = [
        "embeddings",
        "id",
        "metadata",
        "node_id",
        "score",
        "text",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of VectorSearchQueryResponseItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of VectorSearchQueryResponseItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "embeddings": obj.get("embeddings"),
                "id": obj.get("id"),
                "metadata": obj.get("metadata"),
                "node_id": obj.get("node_id"),
                "score": obj.get("score"),
                "text": obj.get("text"),
            }
        )
        return _obj
