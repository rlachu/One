package com.one.testProject;

import org.junit.jupiter.api.Test;


import static org.junit.jupiter.api.Assertions.assertEquals;

class TestCase {

	@Test
	void testSuccess() {
		TestProject testProject = new TestProject();
		assertEquals("foo".toUpperCase(), testProject.getCorrectUpperCase("foo"));
	}
	
	@Test
	void testFailure() {
		TestProject testProject = new TestProject();
		assertEquals("foo".toUpperCase(), testProject.getWrongUpperCase("foo"));
	}
}
