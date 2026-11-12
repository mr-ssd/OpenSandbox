#
# Copyright 2025 The OpenSandbox Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Validation shared by filesystem adapters."""


def validate_unix_mode(mode: int) -> int:
    """Validate octal permission digits represented as a decimal integer."""
    if not isinstance(mode, int) or mode < 0 or mode > 7777 or any(
        digit not in "01234567" for digit in str(mode)
    ):
        raise ValueError("Mode must be octal permission digits from 0 to 7777")
    return mode


def validate_modes(entries) -> None:
    for entry in entries:
        validate_unix_mode(entry.mode)
