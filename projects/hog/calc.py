import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

