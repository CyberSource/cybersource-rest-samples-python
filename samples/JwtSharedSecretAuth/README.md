# JWT Authentication with Shared Secret (HS256)

## Why Migrate from HTTP Signature?

**HTTP Signature authentication is being deprecated.** JWT with Shared Secret is the recommended replacement because:

1. **Same credentials** — Uses the same `merchantKeyId` and `merchantsecretKey` you already have for HTTP Signature. No new credentials needed.
2. **Enables MLE** — Message Level Encryption (MLE) requires JWT authentication. HTTP Signature does not support MLE.
3. **Minimal code change** — Only two properties need to change in your configuration.

## Migration from HTTP Signature

### Before (HTTP Signature)

```python
config = {
    'authentication_type': 'http_signature',
    'merchantid': 'your_merchant_id',
    'merchant_keyid': 'your_key_id',
    'merchant_secretkey': 'your_shared_secret',
    'run_environment': 'apitest.cybersource.com'
}
```

### After (JWT with Shared Secret)

```python
config = {
    'authentication_type': 'jwt',                    # changed
    'jwt_key_type': 'SHARED_SECRET',                 # added
    'merchantid': 'your_merchant_id',
    'merchant_keyid': 'your_key_id',                 # same as before
    'merchant_secretkey': 'your_shared_secret',      # same as before
    'run_environment': 'apitest.cybersource.com'
}
```

That's it. The `merchantKeyId` and `merchantsecretKey` values remain exactly the same.

## Samples in This Folder

| Sample | Description |
|--------|-------------|
| [simple_authorization_with_jwt_shared_secret.py](simple_authorization_with_jwt_shared_secret.py) | Basic payment authorization using JWT + Shared Secret — drop-in replacement for HTTP Signature |
| [mle_payment_with_jwt_shared_secret.py](mle_payment_with_jwt_shared_secret.py) | Payment authorization with MLE enabled — the main benefit of migrating to JWT |

## Configuration

Configuration is defined in [`data/JwtSharedSecretConfiguration.py`](../../data/JwtSharedSecretConfiguration.py):

- `get_merchant_details()` — JWT + Shared Secret (no MLE)
- `get_merchant_details_with_mle()` — JWT + Shared Secret + MLE enabled
- `get_metakey_merchant_details()` — JWT + Shared Secret with MetaKey

## Running the Samples

From the repository root directory:

```bash
# Set PYTHONPATH (if not already set)
export PYTHONPATH=$(pwd):$PYTHONPATH

# Run simple authorization sample
python samples/JwtSharedSecretAuth/simple_authorization_with_jwt_shared_secret.py

# Run MLE-enabled sample
python samples/JwtSharedSecretAuth/mle_payment_with_jwt_shared_secret.py
```

## MLE Certificate

When using MLE with Shared Secret credentials, the MLE public certificate must be provided separately via the `mleForRequestPublicCertPath` property (since there is no P12 file to auto-extract it from).

Download the MLE public certificate from the CyberSource Business Center:

- **Test**: https://businesscentertest.cybersource.com/ebc2
- **Production**: https://businesscenter.cybersource.com/ebc2

Place the certificate in the `resources/` directory and update the path in `get_merchant_details_with_mle()`.

## Comparison of Authentication Types

| Feature | HTTP Signature | JWT with P12 | JWT with Shared Secret |
|---------|---------------|--------------|------------------------|
| Algorithm | HMAC-SHA256 | RS256 (asymmetric) | HS256 (symmetric) |
| Credentials | Key ID + Shared Secret | P12 certificate file | Key ID + Shared Secret |
| MLE Support | No | Yes | Yes |
| Status | **Deprecated** | Active | **Recommended for migration** |

## MetaKey Support

JWT with Shared Secret also supports MetaKey (portfolio-based transactions). Use `get_metakey_merchant_details()` for MetaKey configuration. The portfolio's JWT Shared Secret credentials are used, exactly like HTTP Signature MetaKey.

## Additional Resources

- [CyberSource Python SDK](https://github.com/CyberSource/cybersource-rest-client-python)
- [API Reference Guide](https://developer.cybersource.com/api/reference/api-reference.html)
- [CyberSource Developer Center](https://developer.cybersource.com/)
