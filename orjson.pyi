import datetime
from typing import Optional, Union

def dumps(obj: Union[str, dict, list, tuple, int, float, None], default=Optional[callable]) -> bytes: ...

def loads(obj: Union[bytes, str]) -> Union[dict, list, int, float, str]: ...

class JSONDecodeError(ValueError): ...

class JSONEncodeError(TypeError): ...
