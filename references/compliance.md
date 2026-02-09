# Compliance

Docs entry points:
- `https://docs.x.com/x-api/compliance/batch-compliance/introduction.md`
- `https://docs.x.com/x-api/compliance/create-compliance-job.md`
- `https://docs.x.com/x-api/compliance/get-compliance-job-by-id.md`
- `https://docs.x.com/x-api/compliance/get-compliance-jobs.md`
- `https://docs.x.com/x-api/compliance/streams/introduction.md`

## What This Is

Compliance endpoints help you keep stored X data compliant over time (for example, deletions, withholding, and other state changes).

## Key Endpoints

- `POST /2/compliance/jobs` (create a compliance job)
- `GET /2/compliance/jobs/:id` (inspect job)
- `GET /2/compliance/jobs` (list jobs)

## Create A Compliance Job

Auth (per the OpenAPI docs): Bearer token.
The request body is job-type specific. Use the OpenAPI schema in the docs.

```bash
curl -sS -X POST "https://api.x.com/2/compliance/jobs" \
  -H "Authorization: Bearer $X_BEARER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"type":"..."}'
```

## Get Compliance Job By ID

```bash
JOB_ID="..."

curl -sS "https://api.x.com/2/compliance/jobs/$JOB_ID" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## List Compliance Jobs

```bash
curl -sS "https://api.x.com/2/compliance/jobs" \
  -H "Authorization: Bearer $X_BEARER_TOKEN"
```

## Operational Guidance

- Decide how you will apply compliance updates to your stored data.
- Ensure batch jobs and streams do not create retry storms.
- Keep strong observability (job ids, counts, failures, retries).

## Inventory

### Endpoints

- **POST /2/compliance/jobs** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/compliance/create-compliance-job.md`
- **GET /2/compliance/jobs/{id}** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/compliance/get-compliance-job-by-id.md`
- **GET /2/compliance/jobs** — Auth: `BearerToken` — Doc: `https://docs.x.com/x-api/compliance/get-compliance-jobs.md`

### Docs

- Integration guide: `https://docs.x.com/x-api/compliance/batch-compliance/integrate.md`
- Batch Compliance: `https://docs.x.com/x-api/compliance/batch-compliance/introduction.md`
- Quickstart: `https://docs.x.com/x-api/compliance/batch-compliance/quickstart.md`
- Introduction: `https://docs.x.com/x-api/compliance/streams/introduction.md`
