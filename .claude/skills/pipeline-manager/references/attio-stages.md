# Attio Pipeline Stage Reference

All pipelines are **Lists** in Attio. Use the Lists API, NOT the Deals object.

API Key: stored in `.env` as `ATTIO_API_KEY`
Base URL: `https://api.attio.com/v2`

## To update a stage:
```bash
curl -s -X PUT "https://api.attio.com/v2/lists/{list_id}/entries/{entry_id}" \
  -H "Authorization: Bearer {API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{"data":{"entry_values":{"stage":[{"status":"{status_id}"}]}}}'
```

---

## 1. Outreach: Network Pipeline
**list_id:** `94ccb017-2b86-4e12-b674-e27de8e146c9`

| Stage | status_id |
|-------|-----------|
| Identified | `1509ec8c-0f5f-429e-8606-9fc58ed6b07e` |
| Contacted - Need to Schedule | `c4c61bc9-f98c-474e-af8e-d03d6b4a847d` |
| Call Scheduled | `e1d41c59-8534-46c5-aa3a-9f239e49faff` |
| Need to Reschedule | `4e9cd6f7-ce38-494c-8898-e90b0e1f6740` |
| Need to Send Thank You | `e688c5b0-e866-4dd1-b828-f0ea92a0e64b` |
| Nurture (Quarterly) | `9033782e-c3bf-4fd0-b994-d7dd4e268fd0` |
| Nurture (Occasionally) | `ced8e607-e3bd-40fc-b79b-48aa8cb4db35` |
| Dormant (Revisit Quarterly) | `65e45198-aae0-4740-95e7-fc2df1e03a2b` |

## 2. Outreach: Intermediary Pipeline
**list_id:** `7faac55b-a183-4afe-b7ea-fc8a4ccace10`

| Stage | status_id |
|-------|-----------|
| Identified | `35aa8bcf-2228-41bc-a6fe-d497acacc43a` |
| Contacted | `91cbec2c-e161-419b-8b27-165c39f05339` |
| Warmed | `033e1d56-42ab-43a5-a884-c2aa7ddfcee1` |
| Actively Receiving Deal Flow | `f4869de2-96ab-45c3-897b-6a59dea2ceab` |
| Daily Check in on Matches | `dc675e21-79dc-4cca-8c12-cd851e552e41` |
| Quarterly Check In | `02b86f6c-3997-4840-aca7-a4e41ee9553e` |
| Dormant (Revisit Quarterly) | `6700fdaf-daa4-442e-8374-5382550630bc` |

## 3. Investor Engagement
**list_id:** `f9d58294-5fb2-4794-b796-5c9ffa066025`

| Stage | status_id |
|-------|-----------|
| Q1 | `b47d77db-3d08-4a83-9e03-9f2ed139af99` |
| Q2 | `563fefd2-a527-4367-b712-9fbaa646efda` |
| Q3 | `3cf618a6-1409-415a-b3b8-765b22371364` |
| Q4 | `fb41e66f-b677-4cfa-b50a-0c62a085f20e` |
| YR 2 Q1 | `e9e2aa5e-2856-45e4-b64c-d0bae5d061e9` |
| YR 2 Q2 | `352a4bcb-a992-4d48-85c3-051115685495` |
| YR 2 Q3 | `ec557f47-7f7e-4613-ad12-053b14b20770` |
| YR 2 Q4 | `d1df7804-7d07-4480-89bc-2d38bfa13383` |
| Lost | `532f8709-f603-484c-9104-da21fc30058d` |

## 4. Active Deals – Owners
**list_id:** `0cf5dd92-4a97-4c6b-9f6c-1e64c81bfc7b`

| Stage | status_id |
|-------|-----------|
| Identified | `4c74c706-73ca-4b4c-a207-be47c0f2025f` |
| Contacted | `5c9abae9-9d04-48cf-824f-cb399d580e71` |
| First Conversation | `f6f7ea43-1562-498c-a68e-5581b76b21a4` |
| Second Conversation | `476741ab-a085-448f-8603-d961758f5ab6` |
| NDA Executed | `1728a00f-6e86-444c-9968-c762493a0c45` |
| Financials Received | `4b9d02f9-d17c-49eb-af35-e96f478fc17e` |
| Active Diligence | `33dfbdab-6e92-4a2c-8d01-4c4f598becfe` |
| LOI / Offer Submitted | `11a10867-bd00-45d6-a53b-079faee2cafd` |
| LOI Signed | `4f94cb22-0829-4053-beeb-5883e3b9290e` |
| Closed / Not Proceeding | `c855fed6-cb08-465c-ae68-9885164a76ff` |
