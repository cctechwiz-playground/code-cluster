using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class PlayerController : MonoBehaviour
{
	//Available in editor
	public float speed;
	public Text countText;
	public Text winText;
	//Available only in script
	private Rigidbody rb;
	private int count;

	// Called in the first frame the attached object is created
	void Start()
	{
		// Get handle to the Rigidbody component of Player object
		rb = GetComponent<Rigidbody> ();
		count = 0;
		SetCountText ();
		winText.text = "";
	}

	// Called before rendering a frame (most game code will go here)
	void Update()
	{
		// UNUSED
	}

	// Called before performing physics calculations
	void FixedUpdate()
	{
		// Get input from keyboard
		float moveHorizonatal = Input.GetAxis ("Horizontal");
		float moveVertical = Input.GetAxis ("Vertical");

		// Apply forces to Rigidbody
		Vector3 movement = new Vector3(moveHorizonatal, 0.0f, moveVertical);
		rb.AddForce (movement * speed);
	}

	// Called when Player first touches a trigger collider
	void OnTriggerEnter(Collider other)
	{
		if (other.gameObject.CompareTag ("Pickup"))
		{
			other.gameObject.SetActive (false);
			count++;
			SetCountText ();
		}
	}

	void SetCountText()
	{
		countText.text = "Count: " + count.ToString ();
		if (count >= 13)
		{
			winText.text = "You Win!";
		}
	}
}
