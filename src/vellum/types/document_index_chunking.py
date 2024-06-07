# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from .reducto_chunking import ReductoChunking
from .sentence_chunking import SentenceChunking
from .token_overlapping_window_chunking import TokenOverlappingWindowChunking


class DocumentIndexChunking_ReductoChunker(ReductoChunking):
    chunker_name: typing.Literal["reducto-chunker"] = "reducto-chunker"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class DocumentIndexChunking_SentenceChunker(SentenceChunking):
    chunker_name: typing.Literal["sentence-chunker"] = "sentence-chunker"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class DocumentIndexChunking_TokenOverlappingWindowChunker(TokenOverlappingWindowChunking):
    chunker_name: typing.Literal["token-overlapping-window-chunker"] = "token-overlapping-window-chunker"

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


DocumentIndexChunking = typing.Union[
    DocumentIndexChunking_ReductoChunker,
    DocumentIndexChunking_SentenceChunker,
    DocumentIndexChunking_TokenOverlappingWindowChunker,
]