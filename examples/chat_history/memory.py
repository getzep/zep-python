"""
Example of using the Zep Python SDK asynchronously.

This script demonstrates the following functionality:
- Creating a user.
- Creating a session associated with the created user.
- Adding messages to the session.
- Searching the session memory for a specific query.
- Searching the session memory with MMR reranking.
- Searching the session memory with a metadata filter.
- optionally deleting the session.
"""

import asyncio
import os
import uuid

from dotenv import find_dotenv, load_dotenv

from chat_history_shoe_purchase import history

from zep_cloud.client import AsyncZep
from zep_cloud.types import Message, FactRatingExamples, FactRatingInstruction


load_dotenv(
    dotenv_path=find_dotenv()
)  # load environment variables from .env file, if present

API_KEY = os.environ.get("ZEP_API_KEY") or "YOUR_API_KEY"


async def main() -> None:
    client = AsyncZep(
        api_key=API_KEY,
    )

    # memory = await client.memory.get("8b10e57e99dd4aa49a7d11104333d5e6", min_rating=0.1)
    # print(memory.relevant_facts)

    # search_results = await client.memory.search_sessions(
    #     user_id="0d712b3e24b34b65a6ace08947807825", text="shoes", search_scope="facts", min_fact_rating=0.1
    # )
    # print(search_results)
    # return

#     await client.memory.add(
#         session_id="3c66f0adfbc5486b8901dc261f245030",
#         messages=[Message(role_type="user", role="user", content="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi egestas, sapien nec auctor hendrerit, velit sapien ultrices diam, at maximus lectus neque id ex. Fusce risus libero, vehicula a leo quis, ornare volutpat elit. Maecenas in nunc eget orci porta aliquet vel vel massa. Nulla facilisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ut tellus quis enim ultrices iaculis. Praesent suscipit tempor purus ac bibendum.

# Pellentesque gravida orci enim, eu egestas erat lacinia et. Vestibulum lobortis quam eu ante blandit, in venenatis felis scelerisque. Etiam leo sapien, cursus at pellentesque eget, lacinia sed mauris. Aliquam risus dolor, ullamcorper sed hendrerit et, convallis id dolor. Nulla maximus varius orci, at accumsan mi posuere sit amet. Vestibulum rutrum justo nec nisi tincidunt placerat. Proin dui lorem, condimentum id arcu nec, euismod pretium quam. Nam tempor euismod lorem, eu rhoncus mauris sagittis vel. Morbi at purus ac nunc pellentesque facilisis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nullam vel est id tellus commodo accumsan eget non metus. In ante lacus, sagittis non laoreet quis, tempus auctor sapien. Integer arcu leo, varius ac mollis at, egestas et purus. Aliquam malesuada diam quam. Donec sit amet urna malesuada dolor fermentum vehicula in sed elit.

# Duis tempus libero tortor, in vulputate ligula semper nec. Nulla porttitor ut lacus et fermentum. Integer libero velit, bibendum et sodales at, fringilla vulputate justo. Phasellus viverra interdum arcu, a vulputate est. Proin nibh mauris, consectetur tempor est a, suscipit pharetra ex. Morbi porttitor dapibus lectus non congue. Fusce gravida mi a pulvinar ullamcorper. Sed aliquet feugiat velit, vitae tempor leo scelerisque vitae.

# Praesent bibendum nibh a tincidunt porttitor. Integer lacinia ullamcorper urna nec volutpat. Pellentesque sem turpis, scelerisque a metus non, tempus suscipit eros. Suspendisse commodo ut tortor et scelerisque. Sed ac gravida nibh, eu pharetra ipsum. Quisque mauris velit, rhoncus et justo non, euismod ornare nisl. Nullam mollis consequat justo, vel ullamcorper purus feugiat at. Sed leo nibh, malesuada eu ipsum sed, venenatis facilisis purus. Proin nec tincidunt nunc, a semper dolor. Nam iaculis lacus eu pellentesque venenatis. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Praesent et ante venenatis, elementum leo et, malesuada enim.

# Curabitur eu urna ac elit ornare semper et sed erat. Integer finibus enim imperdiet ultricies ullamcorper. Cras iaculis nibh eget dictum maximus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur vehicula rhoncus lacus, ut luctus mauris pharetra accumsan. Praesent id eleifend nisi, vel malesuada ligula. Ut malesuada purus risus, ac semper est elementum a. Nunc aliquam tincidunt lectus, at tristique mi aliquam sit amet. Morbi dignissim eros ut lacus semper ultricies. Integer quis libero at enim facilisis fermentum.

# Suspendisse potenti. Nullam ultricies sagittis risus porttitor convallis. Quisque laoreet dui id leo porttitor, quis hendrerit turpis suscipit. Proin rhoncus sed mauris ac euismod. Aliquam sit amet laoreet tellus. Fusce fringilla posuere odio, et malesuada ipsum gravida in. Sed venenatis pellentesque odio, in fringilla elit interdum quis.

# Maecenas cursus lectus nec ligula tempus blandit. Praesent eros mauris, commodo dapibus mauris quis, tincidunt interdum mi. Sed feugiat ullamcorper dui, ac dignissim nisi scelerisque a. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Curabitur suscipit aliquam est a scelerisque. In hac habitasse platea dictumst. Aenean dignissim sit amet leo eget bibendum. Duis bibendum condimentum pretium. Praesent dictum sem in metus egestas, iaculis auctor felis vulputate. Donec blandit placerat dignissim. Duis ut euismod arcu, nec interdum urna. Aliquam interdum arcu ultrices sem sodales tempor vitae et arcu.

# Morbi nulla tortor, sagittis at dui vel, congue ullamcorper augue. Donec sit amet lectus laoreet, aliquet mi eget, tincidunt quam. Etiam mollis, justo eu feugiat fermentum, diam lectus elementum lacus, at tincidunt neque leo ut est. Donec in enim facilisis enim pharetra hendrerit. Quisque commodo vel est sit amet dignissim. Fusce id commodo turpis, et feugiat eros. Aenean eget pulvinar sem, et suscipit leo. Vivamus nulla mauris, molestie eu placerat condimentum, condimentum et lacus. Vivamus dignissim erat a velit malesuada ullamcorper. Aliquam erat volutpat. Sed sit amet quam nec nisl interdum auctor. Nam convallis eros neque, sed vehicula lacus lacinia tempus.

# Nam suscipit ex id quam interdum, ac laoreet erat placerat. Donec dignissim posuere lacinia. Duis malesuada orci vel ante tincidunt porta. Mauris in varius lacus. Nam ac lacus vestibulum, imperdiet nulla eu, varius eros. Mauris fringilla pulvinar arcu et suscipit. Sed tempus leo tellus, et dolor.""")],
#     )
    
    # return
    # Create a user
    user_id = uuid.uuid4().hex  # unique user id. can be any alphanum string
    fact_rating_instruction = """Rate the facts by poignancy. Highly poignant 
    facts have a significant emotional impact or relevance to the user. 
    Low poignant facts are minimally relevant or of little emotional 
    significance."""
    fact_rating_examples = FactRatingExamples(
        high="The user received news of a family member's serious illness.",
        medium="The user completed a challenging marathon.",
        low="The user bought a new brand of toothpaste.",
    )
    await client.user.add(
        user_id=user_id,
        email="user@example.com",
        first_name="Jane",
        last_name="Smith",
        metadata={"vip": "true"},
        fact_rating_instruction=FactRatingInstruction(
            instruction=fact_rating_instruction,
            examples=fact_rating_examples,
        )
    )
    # await asyncio.sleep(1)
    print(f"User added: {user_id}")

    session_id = uuid.uuid4().hex  # unique session id. can be any alphanum string

    # Create session associated with the above user
    print(f"\n---Creating session: {session_id}")

    await client.memory.add_session(
        session_id=session_id,
        user_id=user_id,
        metadata={"foo": "bar"},
    )

    # await asyncio.sleep(1)
    # Update session metadata
    print(f"\n---Updating session: {session_id}")
    await client.memory.update_session(session_id=session_id, metadata={"bar": "foo"})
    # await asyncio.sleep(3)
    # Get session
    print(f"\n---Getting session: {session_id}")
    session = await client.memory.get_session(session_id)
    print(f"Session details: {session}")
    # await asyncio.sleep(3)

    # Add Memory for session
    print(f"\n---Add Memory for Session: {session_id}")
    messages = [Message(**m) for m in history]
    await client.memory.add(session_id=session_id, messages=messages)
    # for m in history:
    #     print(f"{m['role']}: {m['content']}")
    #     await client.memory.add(session_id=session_id, messages=[Message(**m)])
    #     # await asyncio.sleep(0.5)

    #  Wait for the messages to be processed
    await asyncio.sleep(50)

    # Synthesize a question from most recent messages.
    # Useful for RAG apps. This is faster than using an LLM chain.
    print("\n---Synthesize a question from most recent messages")
    question = await client.memory.synthesize_question(session_id, last_n_messages=3)
    print(f"Question: {question}")

    # Classify the session.
    # Useful for semantic routing, filtering, and many other use cases.
    print("\n---Classify the session")
    classes = [
        "low spender <$50",
        "medium spender >=$50, <$100",
        "high spender >=$100",
        "unknown",
    ]
    classification = await client.memory.classify_session(
        session_id, name="spender_category", classes=classes, persist=True
    )
    print(f"Classification: {classification}")

    # Get Memory for session
    print(f"\n---Get Perpetual Memory for Session: {session_id}")
    memory = await client.memory.get(session_id)
    print(f"Memory: {memory}")
    print("\n---End of Memory")

    print(f"Memory context: {memory.context}")

    # Search Memory for session
    query = "What are Jane's favorite shoe brands?"
    print(f"\n---Searching over summaries for: '{query}'")
    summary_result = await client.memory.search_sessions(
        session_ids=[session_id], text=query, search_scope="summary"
    )
    print("summaryResult: ", summary_result)

    query = "What are Jane's favorite shoe brands?"
    print(f"\n---Searching over facts for: '{query}'")
    facts_result = await client.memory.search_sessions(
        user_id=user_id, text=query, search_scope="facts"
    )
    print("facts_result: ", facts_result)

    print("\n---Searching over summaries with MMR Reranking")
    summary_mmr_result = await client.memory.search_sessions(
        session_ids=[session_id], text=query, search_scope="summary", search_type="mmr"
    )
    print("summary_mmr_result: ", summary_mmr_result)

    print("\n---Searching over messages using a metadata filter")

    messages_result = await client.memory.search_sessions(
        session_ids=[session_id],
        text=query,
        search_scope="messages",
        record_filter={"where": {"jsonpath": '$[*] ? (@.bar == "foo")'}},
    )
    print("messages_result: ", messages_result)

    user_messages_result = await client.memory.search_sessions(
        limit=3,
        user_id=user_id,
        text=query,
        search_scope="messages",
    )
    print("user_messages_result: ", user_messages_result)

    # End session - this will trigger summarization and other background tasks on the completed session
    # Uncomment to run
    # print(f"\n5---end_session for Session: {session_id}")
    # await client.memory.end_session(session_id)

    # Delete Memory for session
    # Uncomment to run
    # print(f"\n6---deleteMemory for Session: {session_id}")
    # await client.memory.delete(session_id)


if __name__ == "__main__":
    asyncio.run(main())
